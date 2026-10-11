# 05 — System prompts de produção (modo SISTEMA)

Carregue no MODO SISTEMA: system prompt, GPT custom, instrução-mestra, persona de agente.

## O insight central

Uma instrução-mestra reutilizável pode exigir blocos, exemplos e casos-limite. O tamanho deve servir à tarefa: cada bloco precisa justificar seu custo ([curse-of-instructions](../sources/conceitos/curse-of-instructions.md)). A [claude-system-prompts-producao](../sources/fontes/claude-system-prompts-producao.md) registra apenas contexto histórico de uma coleção; seus prompts completos e a comprovação da implementação atual de um produto não fazem parte deste pacote.

## A anatomia de produção (imite esta ordem)

1. **Blocos XML-tagged por domínio de comportamento** — `<citation_instructions>`, `<artifacts_info>`, `<search_instructions>`... Cada bloco isolado, endereçável, substituível. Seu equivalente: uma tag por responsabilidade.
2. **Categorias explícitas com exemplos** — defina quando uma ação cabe, dê exemplos de entradas e descreva o resultado esperado. Categorias como *não buscar / oferecer pesquisa / busca única / pesquisa extensa* podem ajudar quando fizerem sentido para o agente.
3. **Regras de formato por ambiente** — CLI ≤4 linhas; chat com markdown; voz sem listas. O formato é função do ambiente de exibição, não do conteúdo.
4. **Persona, limites e contrato fáceis de localizar** — teste a posição no modelo-alvo; [fim-do-prompt-tem-mais-peso](../sources/conceitos/fim-do-prompt-tem-mais-peso.md) é uma heurística histórica, não uma garantia.
5. **Instruções positivas** — "faça Y" no lugar de "não faça X", exceto nas proibições duras (que são poucas e absolutas).
6. **Separação estável × variável** — a instrução-mestra é estável; o bloco de execução (tarefa, dados, critérios de aceitação) entra por chamada. É o desenho do template de 12 seções descrito em `02-anatomia-do-prompt.md` — use-o como esqueleto (§ objetivo, papel, estilo, ferramentas, saída, processo, checklist, recusas).

## Defesa em profundidade (a lição de runtime)

O system prompt pode ser uma camada de proteção, junto com validação de entrada e saída, controle de acesso às ferramentas e filtros próprios da aplicação. A nota [injecoes-de-seguranca-runtime](../sources/conceitos/injecoes-de-seguranca-runtime.md) registra uma leitura histórica, sem comprovar a arquitetura atual de um produto. Lições práticas: valide fora do modelo e teste entradas adversariais em um ambiente autorizado. **Fronteira: não escrevemos injeção ofensiva contra produtos de terceiros.**

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
