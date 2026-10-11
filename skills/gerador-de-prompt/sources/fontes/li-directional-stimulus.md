# Guiding Large Language Models via Directional Stimulus Prompting

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Guiding Large Language Models via Directional Stimulus Prompting](https://arxiv.org/abs/2302.11520).

Li et al. (UCSB/Microsoft, 2023, NeurIPS) treinam um **policy model pequeno e ajustável (T5, ~780M)** que gera "directional stimulus" — dicas instância-específicas, como keywords para sumarização — inseridas no prompt para guiar um LLM black-box congelado. O policy é otimizado por supervised fine-tuning + RL, usando a métrica final do LLM como reward. Com apenas 4K amostras, melhora o ROUGE do ChatGPT em sumarização (+4-13%) e ganha em geração de diálogo e CoT. Conceito relacionado: [Directional Stimulus Prompting](../conceitos/directional-stimulus-prompting.md).
