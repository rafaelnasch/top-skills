# Active Prompting with Chain-of-Thought for Large Language Models

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Active Prompting with Chain-of-Thought for Large Language Models](https://arxiv.org/abs/2302.12246).

Diao et al. (HKUST, 2023) atacam o ponto fraco do CoT few-shot: os exemplares anotados à mão podem não ser os mais úteis para a tarefa. Inspirados em active learning, propõem medir a **incerteza** do modelo (disagreement/entropia entre k respostas amostradas por questão), selecionar as questões mais incertas para anotação humana de raciocínio, e usar esses exemplares como novos prompts. Supera CoT e [Self-consistency](../conceitos/self-consistency.md) padrão em 8 benchmarks aritméticos/commonsense/simbólicos. Conceito relacionado: [Active-Prompt](../conceitos/active-prompt.md).
