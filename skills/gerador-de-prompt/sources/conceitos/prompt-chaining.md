# Prompt chaining (encadeamento de prompts)

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Prompt chaining** é dividir uma tarefa complexa em subtarefas encadeadas, onde a **saída de um prompt vira a entrada do próximo** — em vez de pedir tudo num prompt gigante, cada elo da corrente faz uma coisa só, bem feita.

Os ganhos são três: **confiabilidade** (cada subtarefa recebe a atenção total do modelo, sem competir com dez instruções — mitiga a [Curse of Instructions](curse-of-instructions.md)), **transparência** (os resultados intermediários são inspecionáveis) e **debugging** (quando a resposta final sai errada, dá pra localizar o elo que falhou e consertar só ele). O exemplo canônico da documentação da Anthropic: em QA sobre documento longo, primeiro um prompt **extrai as citações relevantes**, depois um segundo prompt **responde com base só nelas** — melhor que fazer as duas coisas de uma vez.

É a recomendação padrão da Anthropic para prompts complexos: se o modelo derrapa numa tarefa multi-etapa, quebre em cadeia antes de sofisticar o prompt único. Padrões comuns de cadeia: gerar → criticar → revisar (parente do [Reflexion (reforço verbal)](reflexion.md) e da [Auto-crítica de LLM](auto-critica-de-llm.md)), extrair → transformar → formatar, e roteamento (um prompt classifica, o próximo trata cada caso).

Conceitualmente é a versão determinística e pré-roteirizada do ciclo de execução de agentes: no chaining, **o humano desenha o grafo** e o modelo preenche os nós; no agente, o modelo decide o próximo passo. Essa é a distinção workflow × agente. Cadeias são compostas por um orquestrador externo — código, um estrutura de execução de agentes — e cada elo se beneficia de um bom [Template mestre de prompt (12 seções)](template-mestre-de-prompt.md) e de [Configurações de inferência](configuracoes-de-inferencia.md) próprias (ex.: extração com temperatura baixa, redação com mais alta).

## Conexões
[Engenharia de prompts](engenharia-de-prompts.md) · [Curse of Instructions](curse-of-instructions.md) · ciclo de execução de agentes · estrutura de execução de agentes · [Reflexion (reforço verbal)](reflexion.md) · [Auto-crítica de LLM](auto-critica-de-llm.md) · [Meta-prompting](meta-prompting.md) · [Template mestre de prompt (12 seções)](template-mestre-de-prompt.md) · [Configurações de inferência](configuracoes-de-inferencia.md) · engenharia de contexto

## Fontes
[Chain complex prompts for stronger performance (Anthropic)](../fontes/anthropic-prompt-chaining-docs.md) · [Prompt Engineering Guide (DAIR.AI)](../fontes/prompt-engineering-guide-dair.md)
