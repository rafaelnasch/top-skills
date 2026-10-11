# 02 — O processo de construção (7 passos)

## Passo 1 — Capturar intenção

Extraia o máximo da conversa antes de perguntar. Você precisa de:
- **Especialista/método.** Quem é? (Tim Ferriss, Hormozi, Naval, um método interno do usuário...)
- **A unidade de pensamento dele.** O que ele considera a "unidade" de análise? Brunson = o funil. Ferriss = a restrição. Hormozi = a oferta. Voss = a conversa/emoção. **Isso define o roteador.**
- **Intenções de usuário** que a skill atende (quais pedidos reais devem disparar).
- **Idioma** da skill (voz + conversa).
- **Material disponível** (livros, ePubs, transcrições) pra `sources/`.

Se faltar algo essencial, pergunte de forma enxuta. Não trave; assuma defaults sensatos e siga.

## Passo 2 — Decidir local + verificar convenção

- **Pessoal, Codex:** `~/.agents/skills/<nome>/`.
- **Pessoal, Claude Code:** `~/.claude/skills/<nome>/`.
- **Projeto:** `<projeto>/.agents/skills/<nome>/` ou `<projeto>/.claude/skills/<nome>/`, conforme o agente.
- **Catálogo próprio:** siga a convenção do usuário, se existir. Não presuma scripts externos.
- Confira se o destino já existe. Nunca sobrescreva outra skill sem autorização.
- Crie uma pasta real contendo `SKILL.md`, `references/`, `sources/` e `INGEST.md`.
- Valide `name` (até 64 caracteres, minúsculas, números e hífen, igual à pasta) e `description` (até 450 caracteres).
- Abra uma nova sessão do agente e confirme que a skill foi descoberta.
- Em zsh, use arrays ou nomes literais em loops; não dependa da divisão automática de uma variável sem aspas.

## Passo 3 — Derivar os comportamentos (CRÍTICO)

Leia `03-derive-behaviors.md`. Em uma frase: **não copie os comportamentos de outra persona — re-derive como ESTE especialista pensa.** Mapeie: como ele diagnostica, como decide, como ensina, como fala, o que recusa. Esse passo é o que faz a skill ter alma.

## Passo 4 — Escrever o SKILL.md

Use `templates/SKILL.md.tmpl`. Preencha na ordem da anatomia (`01-architecture.md`). A `description` é o gatilho — invista nela (`04-quality-bar.md`). Mantenha o corpo < ~120 linhas.

## Passo 5 — Escrever as referências curadas

Use `templates/reference.md.tmpl`. Uma por framework. Regras:
- Comece pela `00-canon.md` (voz/visão/léxico) e pela referência do **roteador-mestre** (o diagnóstico de entrada).
- Inclua um `NN-decision-checklist.md` (entry-point "decide a alavanca de X").
- Enxuta (~30–120 linhas), com seção "Como entregar" e ponteiros entre referências.
- Conteúdo real e acionável — protocolos, passos, heurísticas — não resumo vago.

## Passo 6 — Camada de crescimento

- `sources/README.md` a partir de `templates/sources-README.md.tmpl`.
- `INGEST.md` a partir de `templates/INGEST.md.tmpl`.
- Ajuste os caminhos e o nome da skill nos templates.

## Passo 7 — Verificar + (opcional) testar

- Rode a barra de qualidade `04-quality-bar.md` em silêncio; corrija inline.
- `find` na pasta + `wc -l` pra confirmar estrutura e tamanhos.
- Abra uma nova sessão e confirme que a skill foi descoberta pelo agente.
- Se o usuário quiser **teste quantitativo** (rodar a skill em casos reais, comparar com/sem skill, eval viewer), faça handoff pro **skill-creator oficial** — ele tem o maquinário de benchmark. O criar-skill-ouro entrega a skill pronta e bem-estruturada; o skill-creator mede.

## Entrega ao usuário

Sempre feche respondendo, sem o usuário precisar perguntar:
1. **Onde** a skill e os arquivos ficaram.
2. **Como** ela cresce com o tempo (sources/ + INGEST).
3. **Como** usar no dia a dia (invocação direta, intenção natural, pedidos cirúrgicos).
