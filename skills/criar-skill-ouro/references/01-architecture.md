# 01 — Arquitetura de uma skill padrão ouro

## Os três níveis de carregamento (progressive disclosure)

1. **Metadata (name + description)** — sempre no contexto (~100 palavras). É o **gatilho**.
2. **Corpo do SKILL.md** — entra quando a skill dispara. Mantenha < ~120 linhas.
3. **Referências + sources** — carregadas só quando a tabela mandar. Ilimitadas, mas você lê uma por vez.

A regra: o que é raro/grande/específico desce de nível. O que decide o roteamento fica em cima.

## Esqueleto de diretório

```
<nome-da-skill>/
├── SKILL.md
├── INGEST.md
├── references/
│   ├── 00-canon.md                 # voz + visão de mundo + léxico (1ª interação)
│   ├── 01-<framework-principal>.md # diagnóstico de entrada / roteador-mestre
│   ├── 02-<framework>.md ...        # um framework por arquivo
│   └── NN-decision-checklist.md     # entry-point "decide a alavanca de X"
├── templates/   (opcional — só se a skill gera artefatos repetidos)
└── sources/
    └── README.md
```

## Anatomia do SKILL.md (ordem fixa)

1. **Frontmatter YAML** — `name` + `description`. Description pushy e específica (ver `04-quality-bar.md`).
2. **Identidade** (1ª linha do corpo) — "Você é [especialista]. Você não é [o estereótipo raso], você é [a essência operacional]." A voz começa aqui, não no fim.
3. **Loop do roteador** — os passos internos que a skill roda a cada pedido (ler intenção → nomear restrição → rotear pra 1 referência → responder → fechar).
4. **Comportamentos** — as diretrizes de COMO o especialista opera (derivadas, não copiadas).
5. **Tabela de referência** — `| Referência | Quando carregar |` com gatilho explícito por linha.
6. **Camada de crescimento** — ponteiro pra `sources/` + `INGEST.md`.
7. **Fronteiras** — o que a skill recusa.
8. **Princípios de fechamento** — a visão de mundo inegociável (a "constituição").

## Anatomia de uma referência

- Abre dizendo **quando carregar** (espelha o gatilho da tabela).
- O framework em si: conceito → passos/protocolo → heurísticas.
- Uma seção **"Como entregar"** (caso → nomear restrição → decisão → fechamento).
- **Ponteiros** pra outras referências (`→ 03-...md`) onde fizer sentido.
- Rodapé `<!-- fontes: ... ingerido em AAAA-MM-DD -->` pra procedência.

## A camada de crescimento (obrigatória)

- **`sources/`** = inbox de bruto (ePubs, PDFs, transcrições, exports de wiki). Nunca lido em conversa normal.
- **`INGEST.md`** = playbook: bruto → extrair só o durável → destilar na referência certa (ou criar nova + adicionar na tabela do SKILL.md) → registrar procedência.

Sem essa camada, a skill é uma foto. Com ela, é um organismo.

## Decisão de local

- **Pessoal:** `~/.agents/skills/<nome>/` (Codex) ou `~/.claude/skills/<nome>/` (Claude Code).
- **Projeto:** `<projeto>/.agents/skills/<nome>/` ou `<projeto>/.claude/skills/<nome>/`.
- Se existir um catálogo próprio, siga a convenção do usuário.

Confira uma skill existente do mesmo escopo, preserve o destino se já estiver ocupado e valide o frontmatter antes da instalação. Esta distribuição não depende de infraestrutura externa.
