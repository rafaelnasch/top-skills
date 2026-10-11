# 05 — System prompts de produção (modo SISTEMA)

Carregue no MODO SISTEMA: system prompt, GPT custom, instrução-mestra, persona de agente.

## O insight central

O melhor professor de system prompt é um system prompt real de produção. O do claude.ai (extraído pela comunidade; fonte no wiki: [[claude-system-prompts-producao]], raw no Drive) tem **dezenas de milhares de tokens** — o oposto do mito do prompt curto mágico. Produção = longo, estruturado, cheio de exemplos e casos-limite. Mas longo NÃO é despejado: é modular, e cada bloco paga o próprio custo (senão a [[curse-of-instructions]] cobra).

## A anatomia de produção (imite esta ordem)

1. **Blocos XML-tagged por domínio de comportamento** — `<citation_instructions>`, `<artifacts_info>`, `<search_instructions>`... Cada bloco isolado, endereçável, substituível. Seu equivalente: uma tag por responsabilidade.
2. **Categorias explícitas com exemplos** — o claude.ai não diz "busque quando necessário"; define categorias (*nunca buscar / oferecer / busca única / research*) e dá exemplos de queries em cada uma. Comportamento condicional = categorias nomeadas + exemplos, nunca advérbios ("quando apropriado").
3. **Regras de formato por ambiente** — CLI ≤4 linhas; chat com markdown; voz sem listas. O formato é função do ambiente de exibição, não do conteúdo.
4. **Persona e guardrails posicionados no fim** — aproveitando que o [[fim-do-prompt-tem-mais-peso]].
5. **Instruções positivas** — "faça Y" no lugar de "não faça X", exceto nas proibições duras (que são poucas e absolutas).
6. **Separação estável × variável** — a instrução-mestra é estável; o bloco de execução (tarefa, dados, critérios de aceitação) entra por chamada. É o desenho do template de 12 seções descrito em `02-anatomia-do-prompt.md` — use-o como esqueleto (§ objetivo, papel, estilo, ferramentas, saída, processo, checklist, recusas).

## Defesa em profundidade (a lição de runtime)

O system prompt não é a única camada: o claude.ai roda classificadores que **injetam instruções após a mensagem do usuário** quando flagram risco (copyright, conteúdo nocivo) — [[injecoes-de-seguranca-runtime]]. Lições pra quem constrói produto: (a) não confie tudo ao prompt de design-time; valide entrada/saída fora do modelo; (b) instruções tardias têm força — use a posição a seu favor; (c) estude injeção como defesa. **Fronteira: não escrevemos injeção ofensiva contra produtos de terceiros.**

## Heurísticas / regras

- Comece com 3–5 blocos, não 15. Adicione bloco quando um comportamento falhar em teste, não por antecipação (curse of instructions).
- Cada regra abstrata que você escrever, pergunte: "cabe um exemplo aqui?" — o exemplo condiciona mais que a regra.
- Persona sem função é enfeite: cada traço deve mudar uma decisão observável.
- Teste o system prompt com os mesmos 5–10 casos após CADA mudança (`07`) — mudança em bloco A quebra comportamento do bloco B silenciosamente.

## Como entregar

1. Entregue a instrução-mestra completa em blocos tagged, com o bloco de execução separado e um exemplo de chamada preenchida.
2. Aponte as decisões de arquitetura ("categorias de busca com exemplos porque 'quando necessário' não condiciona nada").
3. Feche com a suite mínima: "estes 6 casos cobrem cada bloco; roda depois de toda edição".

## Conexões

- Esqueleto detalhado das 12 seções → `02`. Suite de casos e regressão → `07`. Análise de um system prompt existente → `06`.

<!-- fontes: claude-system-prompts-producao, system-prompt-de-producao, injecoes-de-seguranca-runtime, template-mestre-de-prompt (notas de curadoria), ingerido em 2026-07-05. Atualize via INGEST.md -->
