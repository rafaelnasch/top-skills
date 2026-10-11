# Self-Consistency Improves Chain of Thought Reasoning in Language Models

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171).

Wang et al. (Google, 2022) propõem trocar o greedy decoding do [Chain-of-Thought (CoT)](../conceitos/chain-of-thought.md) por **sample-and-marginalize**: amostrar múltiplos caminhos de raciocínio diversos (temperature sampling) e escolher a resposta mais consistente por votação majoritária. A intuição: problemas complexos admitem vários caminhos válidos que convergem na mesma resposta correta. Ganhos expressivos sem treino extra — GSM8K +17.9%, SVAMP +11.0%, AQuA +12.2% sobre CoT padrão. Conceito relacionado: [Self-consistency](../conceitos/self-consistency.md).
