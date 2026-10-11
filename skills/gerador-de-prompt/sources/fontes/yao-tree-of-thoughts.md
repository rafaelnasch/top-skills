# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601).

Yao et al. (Princeton/DeepMind, 2023) generalizam o [Chain-of-Thought (CoT)](../conceitos/chain-of-thought.md) para uma **árvore de pensamentos**: o LLM gera múltiplos "thoughts" intermediários, autoavalia cada estado e explora a árvore com busca deliberada (BFS/DFS), com lookahead e backtracking — raciocínio "System 2" em vez do decoding left-to-right. No Game of 24, GPT-4 com CoT resolve só 4% das tarefas; com ToT, **74%**. Também ganha em Creative Writing e Mini Crosswords. Conceito relacionado: [Tree of Thoughts (ToT)](../conceitos/tree-of-thoughts.md).
