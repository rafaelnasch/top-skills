# ReAct prompting (Reason + Act)

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**ReAct** (Yao et al., 2022 — arXiv:2210.03629) é o padrão de prompting que intercala traços de raciocínio e ações sobre um ambiente externo num loop **Thought → Action → Observation**: o modelo pensa, executa uma ação (buscar na Wikipedia, chamar uma API), observa o resultado e volta a pensar com a informação nova no contexto.

A sacada é sinergia: o raciocínio ([Chain-of-Thought (CoT)](chain-of-thought.md)) ajuda o modelo a planejar e ajustar o plano de ação, enquanto as ações deixam ele **consultar o mundo real** em vez de confabular de memória. Em CoT puro, o modelo raciocina sobre uma representação interna estática — e alucina fatos. No ReAct, cada `Observation` injeta evidência fresca, o que reduziu alucinação factual nos benchmarks **HotpotQA** (QA multi-hop) e **FEVER** (verificação de fatos) frente ao CoT puro; a melhor configuração do paper combina os dois (ReAct + CoT com [Self-consistency](self-consistency.md)). Em ambientes interativos (ALFWorld, WebShop), ReAct com 1-2 exemplos superou métodos de imitação e RL.

Na prática, ReAct é um caso de [Few-shot prompting](few-shot-prompting.md): as demonstrações mostram trajetórias completas Thought/Action/Observation e o modelo imita o formato. Quem executa a ação e devolve a observação não é o modelo — é o software em volta. Por isso ReAct é a **semente do ciclo de execução de agentes e do estrutura de execução de agentes moderno**: tool use nativo, function calling e protocolos como Model Context Protocol (MCP) são a industrialização desse padrão, e a distinção entre quem raciocina e quem executa é exatamente separação entre modelo e estrutura de execução.

Limitações conhecidas: sem raciocínio de qualidade o loop degenera (buscas repetidas, loops infinitos), e o desempenho depende muito das tools disponíveis. Parentes próximos: [PAL — Program-Aided Language Models](pal.md) (delegar computação a um interpretador) e [ART — Automatic Reasoning and Tool-use](art-automatic-reasoning-tool-use.md) (selecionar demonstrações de tool use automaticamente).

## Conexões
[Chain-of-Thought (CoT)](chain-of-thought.md) · ciclo de execução de agentes · estrutura de execução de agentes · separação entre modelo e estrutura de execução · Model Context Protocol (MCP) · [PAL — Program-Aided Language Models](pal.md) · [ART — Automatic Reasoning and Tool-use](art-automatic-reasoning-tool-use.md) · [RAG — Retrieval-Augmented Generation](rag.md) · [Few-shot prompting](few-shot-prompting.md) · [Self-consistency](self-consistency.md) · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[Prompt Engineering Guide (DAIR.AI)](../fontes/prompt-engineering-guide-dair.md)
