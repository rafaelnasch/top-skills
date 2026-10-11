# ART — Automatic Reasoning and Tool-use

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**ART (Automatic Reasoning and Tool-use)** (Paranjape et al., 2023) é um framework que monta automaticamente o prompt de raciocínio multi-step com uso de ferramentas: dado um problema novo, ele **seleciona demonstrações de uma task library** (tarefas parecidas resolvidas passo a passo, com chamadas de tool) e as usa como few-shot — sem ninguém escrever o [Chain-of-Thought (CoT)](chain-of-thought.md) à mão para cada tarefa.

O mecanismo de execução é o detalhe elegante: o LLM congelado vai gerando os passos num formato de programa e, quando o passo invoca uma ferramenta externa (busca, execução de código), o framework **congela a geração, roda a tool e retoma a geração** com o resultado inserido no contexto. É o mesmo contrato do [ReAct prompting (Reason + Act)](react-prompting.md) — raciocínio do modelo, execução do ambiente — mas com a seleção de demonstrações automatizada em vez de exemplos fixos escritos à mão, e o formato programático herdado do [PAL — Program-Aided Language Models](pal.md).

Nos benchmarks (tarefas não vistas do BigBench e MMLU), ART igualou ou superou o CoT artesanal, e ficou competitivo com os melhores prompts feitos à mão quando a tool certa estava disponível. E é **extensível por humanos**: dá pra melhorar o desempenho numa tarefa específica só editando/adicionando entradas na task library ou na tool library — feedback humano barato, sem retreinar nada.

ART antecipa duas ideias que viraram infraestrutura: bibliotecas de tools plugáveis (hoje padronizadas em coisas como Model Context Protocol (MCP)) e a seleção dinâmica de demonstrações — parente do [Active-Prompt](active-prompt.md) (que escolhe o que anotar) e um passo na direção da [Otimização automática de prompts](otimizacao-automatica-de-prompts.md).

## Conexões
[ReAct prompting (Reason + Act)](react-prompting.md) · [PAL — Program-Aided Language Models](pal.md) · [Chain-of-Thought (CoT)](chain-of-thought.md) · [Few-shot prompting](few-shot-prompting.md) · [Active-Prompt](active-prompt.md) · ciclo de execução de agentes · estrutura de execução de agentes · Model Context Protocol (MCP) · [Otimização automática de prompts](otimizacao-automatica-de-prompts.md)

## Fontes
[ART: Automatic multi-step reasoning and tool-use for large language models](../fontes/paranjape-art.md)
