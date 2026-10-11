#!/usr/bin/env python3
"""Valida a distribuição e os ZIPs sem executar as skills ou suas integrações."""
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'criar-skill-ouro', 'gerador-de-prompt', 'book-to-skill', 'humanizer',
    'last30days', 'notebooklm', 'elliott-jaques', 'jesus-cristo',
}


def frontmatter(text):
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        raise ValueError('frontmatter ausente')
    block = match.group(1)
    name_match = re.search(r'^name:\s*(.+)$', block, re.M)
    desc_match = re.search(r'^description:([^\n]*)(?:\n((?:[ \t]+[^\n]*(?:\n|$))*))?', block, re.M)
    if not name_match or not desc_match:
        raise ValueError('name ou description ausente')
    name = name_match.group(1).strip().strip('"\'')
    value = desc_match.group(1).strip()
    if value in ('>', '|', '>-', '|-'):
        description = ' '.join(line.strip() for line in (desc_match.group(2) or '').splitlines())
    elif value.startswith('"'):
        description = json.loads(value)
    elif value.startswith("'"):
        description = value[1:-1].replace("''", "'")
    else:
        description = value
    return name, description


def main():
    if sys.version_info < (3, 12):
        print('Use Python 3.12 ou superior para validar também os scripts de Last 30 Days.')
        return 1
    errors = []
    skill_dirs = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
    if skill_dirs != EXPECTED:
        errors.append('O conjunto de skills difere das oito esperadas.')
    manifest = json.loads((ROOT / 'manifest.json').read_text())
    if {x['name'] for x in manifest['skills']} != EXPECTED or len(manifest['skills']) != 8:
        errors.append('O manifesto deve conter as oito skills, sem duplicação.')
    source_total = 0
    for entry in manifest['skills']:
        directory = ROOT / entry['path']
        try:
            name, description = frontmatter((directory / 'SKILL.md').read_text())
            if name != directory.name or not re.fullmatch(r'[a-z0-9-]{1,64}', name):
                errors.append(f'{entry["name"]}: name inválido.')
            if not 1 <= len(description) <= 450:
                errors.append(f'{name}: description excede o limite ou está vazia.')
        except (ValueError, OSError) as error:
            errors.append(f'{entry["name"]}: {error}')
        members = {f'{directory.name}/{p.relative_to(directory)}': p.read_bytes()
                   for p in directory.rglob('*') if p.is_file()}
        if len(members) != entry['files']:
            errors.append(f'{directory.name}: contagem de arquivos divergente.')
        archive = ROOT / entry['zip']
        if hashlib.sha256(archive.read_bytes()).hexdigest() != entry['archive_sha256']:
            errors.append(f'{directory.name}: SHA-256 do ZIP divergente.')
        with zipfile.ZipFile(archive) as z:
            if z.testzip() is not None:
                errors.append(f'{directory.name}: ZIP corrompido.')
            if set(z.namelist()) != set(members) or len(z.namelist()) != len(members):
                errors.append(f'{directory.name}: conteúdo do ZIP divergente.')
            for member, data in members.items():
                if z.read(member) != data:
                    errors.append(f'{directory.name}: ZIP contém versão antiga de {member}.')
        # Referências estáticas mencionadas no roteador principal.
        for relative in re.findall(r'`((?:references|assets|templates|sources)/[\w.-]+\.(?:md|tmpl))`',
                                   (directory / 'SKILL.md').read_text()):
            if not (directory / relative).is_file():
                errors.append(f'{directory.name}: referência ausente: {relative}')
        source_dir = directory / 'sources'
        index = source_dir / 'README.md'
        if not index.is_file():
            errors.append(f'{directory.name}: índice de fontes ausente.')
        source_files = sorted(p for p in source_dir.rglob('*') if p.is_file())
        actual = [{'path': str(p.relative_to(directory)),
                   'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
                  for p in source_files]
        if actual != entry.get('source_files'):
            errors.append(f'{directory.name}: inventário ou hash das fontes divergente.')
        count = len([p for p in source_files if p != index])
        if not count or count != entry.get('source_materials'):
            errors.append(f'{directory.name}: contagem de materiais de fontes divergente.')
        source_total += count
        for path in source_files:
            text = path.read_text()
            if re.search(r'\[\[[^\]\n]+\]\]', text):
                errors.append(f'{path.relative_to(ROOT)}: wikilink sem resolução.')
            for target in re.findall(r'\[[^\]\n]+\]\(([^\s)]+)\)', text):
                parsed = urlsplit(target.strip('<>'))
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                destination = (path.parent / unquote(parsed.path)).resolve()
                if not destination.is_relative_to(ROOT) or not destination.exists():
                    errors.append(f'{path.relative_to(ROOT)}: vínculo local ausente: {target}')
    if source_total != manifest.get('source_materials'):
        errors.append('Contagem total de materiais de fontes divergente.')

    private_path = re.compile(r'/Users/macbook|~/cerebros|~/wiki|growai-estacao|brain-pessoal|/home/(?:jp|ubuntu)|ssh vps')
    private_source = re.compile(r'\b(?:GrowAI|GrowAura|Rafael|Nasch|Clau|Nora)\b|/Users/|/home/(?:jp|ubuntu)|~/cerebros|~/wiki|brain-pessoal|(?:drive|docs)\.google\.com|(?:app\.)?clickup\.com', re.I)
    secret = re.compile(r'gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{50,}|sk-[A-Za-z0-9_-]{35,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----')
    for path in ROOT.rglob('*'):
        relative = path.relative_to(ROOT)
        if '.git' in relative.parts:
            if relative.parts[0] != '.git':
                errors.append(f'{relative}: repositório Git aninhado.')
            continue
        if path.is_symlink():
            errors.append(f'{relative}: link simbólico não permitido.')
        if not path.is_file() or path.suffix == '.zip':
            continue
        if path.name == '.env' or path.name.startswith('.env.') or path.name in ('storage_state.json', 'context.json'):
            errors.append(f'{relative}: arquivo de ambiente ou autenticação não permitido.')
        text = path.read_text()
        # O próprio validador contém as expressões de detecção, não segredos.
        if path != Path(__file__).resolve():
            for number, line in enumerate(text.splitlines(), 1):
                if private_path.search(line):
                    errors.append(f'{relative}:{number}: caminho privado residual.')
                if secret.search(line):
                    errors.append(f'{relative}:{number}: padrão de segredo detectado; valor omitido.')
                if relative.parts[0] == 'skills' and 'sources' in relative.parts and private_source.search(line):
                    errors.append(f'{relative}:{number}: marcador de contexto privado nas fontes; conteúdo omitido.')
        if path.suffix == '.py':
            try:
                ast.parse(text, filename=str(relative))
            except SyntaxError as error:
                errors.append(f'{relative}:{error.lineno}: sintaxe Python inválida.')
        if path.suffix == '.json':
            try:
                json.loads(text)
            except ValueError:
                errors.append(f'{relative}: JSON inválido.')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'OK: 8 skills; {source_total} materiais de fontes com hashes e vínculos válidos; descriptions até 450 caracteres; referências presentes; 8 ZIPs íntegros e idênticos às pastas; sintaxe Python e JSON válidos; nenhuma ocorrência nos padrões de contexto privado ou segredo verificados.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
