# RLHF — RL a partir de feedback humano

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**RLHF (Reinforcement Learning from Human Feedback)** é treinar um modelo por reforço usando como recompensa um **reward model aprendido de preferências humanas**: humanos comparam pares de saídas ("qual das duas é melhor?"), o reward model aprende a prever essas preferências, e a política é otimizada contra ele — substituindo a função de recompensa que ninguém sabe escrever à mão.

A origem é Christiano et al. (2017, *Deep RL from Human Preferences*): humanos comparavam **pares de trajetórias** curtas de agentes (Atari, MuJoCo) e o método aprendia comportamentos sem recompensa programada — o exemplo icônico é ensinar um simulado a dar **backflip com ~900 bits de feedback humano** (menos de uma hora de trabalho de avaliador), comportamento que seria dificílimo de especificar como função. A tese: pra objetivos complexos e mal-especificáveis, **comparar é muito mais fácil que definir** — e barato o suficiente pra escalar.

Aplicado a LLMs, o pipeline canônico (InstructGPT, Ouyang et al., 2022 — a base do ChatGPT) tem três etapas: (1) SFT em demonstrações — o [Instruction tuning](instruction-tuning.md); (2) reward model treinado em **rankings de respostas** feitos por humanos; (3) otimização da política com PPO contra o reward model. O resultado do paper que resume tudo: o InstructGPT de **1,3B** parâmetros foi preferido pelos avaliadores ao GPT-3 de **175B** sem RLHF — alinhamento comprou mais utilidade percebida que 100x de escala.

Para a [Engenharia de prompts](engenharia-de-prompts.md), RLHF é o solo em que tudo cresce: é **o motivo de modelos seguirem instruções** e de o [Zero-shot prompting](zero-shot-prompting.md) funcionar — um modelo base só pré-treinado (previsão do próximo token em transformers) completa texto, não obedece. O par [Instruction tuning](instruction-tuning.md) + RLHF transformou "complete este texto" em "faça o que eu pedi", viabilizando a interface de linguagem natural do programação por contexto. Efeitos colaterais também vêm daí: bajulação (sycophancy), verbosidade e respostas-padrão são vieses do que os avaliadores preferiram. Variações posteriores: RLAIF/Constitutional AI (Anthropic, feedback de IA guiado por princípios) e DPO (otimização direta de preferências, sem RL explícito).

## Conexões
[Instruction tuning](instruction-tuning.md) · [Zero-shot prompting](zero-shot-prompting.md) · programação por contexto · previsão do próximo token em transformers · [Directional Stimulus Prompting](directional-stimulus-prompting.md) · [Soft prompts (prompts contínuos)](soft-prompts.md) · [Engenharia de prompts](engenharia-de-prompts.md) · determinismo e variabilidade

## Fontes
[Deep Reinforcement Learning from Human Preferences](../fontes/christiano-rl-human-preferences.md)
