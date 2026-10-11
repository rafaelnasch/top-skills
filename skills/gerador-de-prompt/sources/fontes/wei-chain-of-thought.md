# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903).

Wei et al. (Google Brain, 2022) mostram que incluir exemplos few-shot com passos intermediários de raciocínio ("chains of thought") destrava reasoning em LLMs grandes — é uma **emergent ability** que só aparece em escala (~100B+ parâmetros). Com apenas 8 exemplares de CoT, o PaLM 540B atinge 56.9%+ no GSM8K (state of the art na época, superando GPT-3 finetunado com verifier), com ganhos também em raciocínio simbólico e commonsense. O paper fundou a família inteira de técnicas de prompting de raciocínio. Conceito relacionado: [Chain-of-Thought (CoT)](../conceitos/chain-of-thought.md).
