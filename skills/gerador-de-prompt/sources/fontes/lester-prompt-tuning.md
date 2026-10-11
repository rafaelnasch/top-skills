# The Power of Scale for Parameter-Efficient Prompt Tuning

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [The Power of Scale for Parameter-Efficient Prompt Tuning](https://arxiv.org/abs/2104.08691).

Lester et al. (2021, Google): simplifica o prefix-tuning ao treinar só uma sequência de soft prompt tokens prepended ao input, mantendo todo o modelo congelado. A descoberta central é o efeito da escala: no T5-XXL (11B), o prompt tuning empata com o fine-tuning completo do modelo, fechando o gap que existia em modelos menores. Também mostra ganhos de robustez a domain shift e viabiliza "prompt ensembling" barato. Conceito relacionado: [Soft prompts (prompts contínuos)](../conceitos/soft-prompts.md).
