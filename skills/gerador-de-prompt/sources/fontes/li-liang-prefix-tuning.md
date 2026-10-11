# Prefix-Tuning: Optimizing Continuous Prompts for Generation

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Prefix-Tuning: Optimizing Continuous Prompts for Generation](https://arxiv.org/abs/2101.00190).

Li & Liang (2021): congela o LM inteiro e otimiza apenas um "prefixo" de vetores contínuos task-specific — cerca de 0,1% dos parâmetros. Em table-to-text (GPT-2) e sumarização (BART), alcança desempenho comparável ao fine-tuning completo e o supera em regimes de poucos dados e extrapolação. Inaugurou a ideia de prompt como parâmetro treinável em vez de texto discreto. Conceito relacionado: [Soft prompts (prompts contínuos)](../conceitos/soft-prompts.md).
