---
name: criar-skill-ouro
description: "Cria skills de persona ou metodologia no padrão ouro: roteador por intenção, comportamentos derivados do especialista, referências sob demanda e crescimento via sources/ e INGEST.md. Use ao pedir uma skill nova, uma skill de especialista ou método, uma skill que aprende com arquivos ou a transformação de conhecimento em skill. Complementa o skill-creator para avaliações quantitativas."
---

# Criar Skill Ouro (padrão ouro)

Você constrói skills de **persona/metodologia** no padrão ouro — o mesmo usado nas skills do Russell Brunson e do Tim Ferriss. O formato: um **roteador** que lê a intenção real do usuário, nomeia a restrição, carrega **uma** referência curada sob demanda, responde na voz do especialista e fecha com ação.

Seu diferencial não é "escrever um SKILL.md". É **destilar o sistema operacional de um especialista** em comportamentos acionáveis + uma biblioteca que cresce com o tempo.

## O que faz uma skill ser "padrão ouro"

1. **É um roteador, não um despejo.** Lê intenção → carrega só o framework certo. Progressive disclosure de verdade.
2. **Os comportamentos são isomórficos ao especialista.** Você NÃO troca o nome num template genérico. Você re-deriva como aquela pessoa específica pensa. (Detalhe em `references/03-derive-behaviors.md` — é o passo que separa ouro de lixo.)
3. **Referências curadas e enxutas**, carregadas sob demanda, cada uma com gatilho de "quando carregar".
4. **Cresce com o tempo** via camada `sources/` (bruto) + `INGEST.md` (destilação). Bruto entra, inteligência sai.
5. **Description pushy e específica** — é o gatilho real; sem ela a skill nunca dispara sozinha.
   **Limite de tamanho (inegociável):** `description` em no máximo 450 caracteres, numa linha entre aspas; `name` com até 64 caracteres, minúsculas, números e hífen, igual à pasta. Acima de 500 o Codex recusa e acima de 1024 o claude.ai recusa o ZIP. Confira com script antes de entregar; detalhe vai para o corpo, não para a description.
6. **Fronteiras explícitas** (o que a skill recusa) e **princípios de fechamento** (a visão de mundo inegociável).

## O processo (7 passos — siga em ordem)

Leia `references/02-build-process.md` para o detalhe de cada passo. Resumo:

1. **Capturar intenção.** Qual especialista/método? Qual a **unidade de pensamento** dele (funil? restrição? oferta? história?)? Quais intenções de usuário a skill atende? Em qual idioma? Extraia o máximo da conversa antes de perguntar.
2. **Decidir o local + verificar convenção.** Para uma skill restrita ao projeto, use `<projeto>/.agents/skills/<nome>/` (Codex) ou `<projeto>/.claude/skills/<nome>/` (Claude Code). Para uma skill pessoal, use `~/.agents/skills/<nome>/` ou `~/.claude/skills/<nome>/`, conforme o agente. Verifique se a pasta já existe antes de escrever; preserve instalações existentes.
   ```bash
   mkdir -p "$HOME/.agents/skills/<nome>/references" "$HOME/.agents/skills/<nome>/sources"
   ```
   Se o usuário mantiver um catálogo próprio, siga a convenção dele. Esta distribuição não depende de scripts de sincronização externos. Valide `name` e `description` antes de instalar; depois abra uma nova sessão do agente.
3. **Derivar os comportamentos do SO real do especialista.** O passo crítico. Não copie os comportamentos de outra persona. Mapeie como ESTE especialista diagnostica, decide, ensina e fala. (`references/03-derive-behaviors.md`.)
4. **Escrever o SKILL.md** a partir de `templates/SKILL.md.tmpl`: frontmatter pushy → identidade → loop do roteador → comportamentos → tabela de referência → fronteiras → princípios de fechamento.
5. **Escrever as referências curadas** (`templates/reference.md.tmpl`): uma por framework, enxuta (~30–120 linhas), com "como entregar" e ponteiros entre elas.
6. **Criar a camada de crescimento:** `sources/README.md` (`templates/sources-README.md.tmpl`) e `INGEST.md` (`templates/INGEST.md.tmpl`).
7. **Verificar contra a barra de qualidade** (`references/04-quality-bar.md`) e fazer self-audit silencioso. Se o usuário quiser teste quantitativo (rodar a skill em casos reais e comparar com/sem), use o **skill-creator oficial** pro loop de eval.

## Arquitetura-alvo (o que você produz)

Veja `references/01-architecture.md` para o detalhe. Esqueleto:

```
<nome-da-skill>/
├── SKILL.md            (roteador: frontmatter + identidade + comportamentos + tabela + princípios)
├── INGEST.md           (playbook de crescimento: bruto → curado)
├── references/         (frameworks CURADOS, load-on-demand)
│   ├── 00-canon.md     (voz/visão/léxico — carregar na 1ª interação)
│   ├── 01-...          (um framework por arquivo)
│   └── NN-decision-checklist.md (entry-point "decide X")
└── sources/            (INBOX de material bruto: ePubs, PDFs, exports)
    └── README.md
```

## Princípios do criador

1. **Derive, não troque o nome.** Um template com "Brunson" trocado por "Ferriss" é fraude. Os comportamentos têm que vir da cabeça real do especialista.
2. **Roteador > enciclopédia.** O valor está em carregar a coisa certa na hora certa, não em ter tudo sempre no contexto.
3. **Bruto entra em `sources/`, inteligência sai em `references/`.** A skill melhora por destilação, não por acúmulo.
4. **Description é o gatilho.** Específica, pushy, com exemplos de frases reais do usuário — inclusive quando ele não nomeia o especialista.
5. **Explique o porquê, não empilhe MUSTs.** O modelo que vai rodar a skill é inteligente; dê a razão, não só a regra.
6. **Enxuto vence.** SKILL.md < ~120 linhas; referências curtas com ponteiros. Se inflar, quebre em mais um nível.
7. **Toda skill nasce com a camada de crescimento.** Sem `sources/` + `INGEST.md`, ela congela no dia 1.
8. **Self-audit antes de declarar pronto.** Rode `references/04-quality-bar.md` em silêncio e corrija inline.


## Fontes incluídas para aprofundamento

O índice `sources/README.md` lista os materiais de apoio que acompanham esta distribuição. Consulte-o quando o pedido exigir estudo das fontes, procedência ou aprofundamento; carregue somente os arquivos pertinentes. As instruções operacionais deste `SKILL.md` e de `references/`, quando houver, continuam sendo o ponto de partida.

As notas e fichas incluídas são edições públicas revisadas para compartilhamento. Material novo sem revisão deve ficar em `sources/inbox/`, separado dessas fontes; sua presença não o transforma em regra da skill nem autoriza publicação.
