# Directional Stimulus Prompting

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Directional Stimulus Prompting (DSP)** (Li et al., 2023) usa um **policy model pequeno e ajustável** — um T5 da ordem de centenas de milhões de parâmetros — para gerar, por instância, um "estímulo direcional": hints como palavras-chave que são anexadas ao prompt e **direcionam a geração do LLM grande, que permanece congelado**.

O treino do policy model tem duas fases: fine-tuning supervisionado com pseudo-hints extraídos dos dados (ex.: keywords presentes no resumo de referência) e depois **reinforcement learning** cuja recompensa é a métrica da tarefa avaliada na saída do LLM (ROUGE em sumarização, avaliação da resposta em diálogo). Ou seja: aprende-se a *dica* que maximiza o desempenho do modelo grande — otimização indireta, pelo prompt, do comportamento de um black-box.

O resultado ilustrativo do paper: em sumarização (CNN/DailyMail), keywords geradas pelo policy model melhoraram o ROUGE do ChatGPT usando poucos exemplos rotulados; ganhos análogos em diálogo (MultiWOZ) e em CoT. O ponto conceitual é maior que os números: **controle sem mexer nos pesos do modelo grande** — quando o modelo é caro, fechado ou de terceiros, a alavanca de otimização vira o contexto, não o gradiente.

DSP ocupa um ponto interessante do espectro da [Otimização automática de prompts](otimizacao-automatica-de-prompts.md): o estímulo é **discreto e legível** (palavras, não vetores como em [Soft prompts (prompts contínuos)](soft-prompts.md)), mas **aprendido por gradiente/RL** (não buscado por um LLM como em [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) e [OPRO — LLM como otimizador](opro-llm-como-otimizador.md)) e **por instância** (não um prompt fixo pra tarefa). O uso de RL sobre um sinal de preferência/qualidade ecoa a mecânica do [RLHF — RL a partir de feedback humano](rlhf.md) — só que aplicada ao prompt em vez do modelo.

## Conexões
[Otimização automática de prompts](otimizacao-automatica-de-prompts.md) · [Soft prompts (prompts contínuos)](soft-prompts.md) · [RLHF — RL a partir de feedback humano](rlhf.md) · [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) · [OPRO — LLM como otimizador](opro-llm-como-otimizador.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [Elementos de um prompt](elementos-de-um-prompt.md) · [Chain-of-Thought (CoT)](chain-of-thought.md)

## Fontes
[Guiding Large Language Models via Directional Stimulus Prompting](../fontes/li-directional-stimulus.md)
