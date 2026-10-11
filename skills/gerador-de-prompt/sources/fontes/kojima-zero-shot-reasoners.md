# Large Language Models are Zero-Shot Reasoners

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916).

Kojima et al. (U. Tokyo/Google, 2022) descobrem que basta acrescentar **"Let's think step by step"** antes da resposta para eliciar raciocínio multi-step sem nenhum exemplar — o Zero-shot-CoT. Com InstructGPT (text-davinci-002), a acurácia no MultiArith salta de 17.7% para 78.7% e no GSM8K de 10.4% para 40.7%. Pipeline em dois estágios (extrai raciocínio, depois extrai resposta) e evidência de que LLMs são "decent zero-shot reasoners" escondidos atrás do prompt certo. Conceito relacionado: [Zero-shot CoT ("Let's think step by step")](../conceitos/zero-shot-cot.md).
