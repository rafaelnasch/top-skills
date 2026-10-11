# Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL](https://arxiv.org/abs/2309.06553).

Paper do Prompt-OIRL (Sun et al., 2023): parte da observação de que o melhor prompt varia por query — nenhum prompt é ótimo pra todas. Usa offline inverse RL sobre dados de benchmarking já existentes pra aprender um reward model que avalia prompts query-dependent sem chamar o LLM, e então seleciona o melhor prompt por pergunta a custo quase zero. Validado em raciocínio aritmético (GSM8K, SVAMP, MAWPS) com múltiplos LLMs. Conceito relacionado: [Otimização automática de prompts](../conceitos/otimizacao-automatica-de-prompts.md).
