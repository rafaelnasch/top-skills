# Multimodal Chain-of-Thought Reasoning in Language Models

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Multimodal Chain-of-Thought Reasoning in Language Models](https://arxiv.org/abs/2302.00923).

Zhang et al. (Shanghai Jiao Tong/Amazon, 2023) estendem o [Chain-of-Thought (CoT)](../conceitos/chain-of-thought.md) para visão+linguagem com um framework em **dois estágios: gerar o rationale (fundido com features visuais) e só depois inferir a resposta** — separação que reduz alucinação de raciocínio causada por rationales enganosos. Com um modelo de menos de 1B de parâmetros, supera o GPT-3.5 em ~16 pontos (75.17% → 91.68%) no ScienceQA, batendo inclusive a performance humana no benchmark. Conceito relacionado: [Multimodal CoT](../conceitos/multimodal-cot.md).
