# Large Language Model Guided Tree-of-Thought

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Large Language Model Guided Tree-of-Thought](https://arxiv.org/abs/2305.08291).

Long (2023), concorrente e independente do paper de Yao et al., propõe um Tree-of-Thought guiado por um sistema multi-módulo: um **ToT controller** (potencialmente treinado via RL), um prompter agent, um checker e um módulo de memória orquestram o LLM na exploração da árvore com backtracking. A diferença chave: enquanto o ToT de Yao usa busca genérica (BFS/DFS), aqui o controller aprende com dados e pode evoluir. Validado em Sudoku, onde eleva significativamente a taxa de acerto sobre zero-shot, one-shot e few-shot CoT. Conceito relacionado: [Tree of Thoughts (ToT)](../conceitos/tree-of-thoughts.md).
