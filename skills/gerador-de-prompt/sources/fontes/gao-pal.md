# PAL: Program-aided Language Models

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [PAL: Program-aided Language Models](https://arxiv.org/abs/2211.10435).

Gao et al. (CMU, 2022) separam **entender do computar**: o LLM lê o problema e gera passos de raciocínio como código Python, mas delega a execução a um interpretador — eliminando os erros aritméticos/lógicos que o [Chain-of-Thought (CoT)](../conceitos/chain-of-thought.md) em linguagem natural comete mesmo quando decompõe certo. Com Codex, PAL supera o PaLM-540B+CoT no GSM8K em ~15 pontos absolutos (top-1), com state of the art nos 13 benchmarks de raciocínio matemático, simbólico e algorítmico do BIG-Bench Hard testados. Conceito relacionado: [PAL — Program-Aided Language Models](../conceitos/pal.md).
