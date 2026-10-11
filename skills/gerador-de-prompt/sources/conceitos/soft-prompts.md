# Soft prompts (prompts contínuos)

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Soft prompts** são prompts contínuos aprendidos por gradiente: em vez de palavras, **vetores treináveis no espaço de embeddings** que são prepostos à entrada, enquanto todos os pesos do modelo ficam congelados. O "prompt" deixa de ser texto e vira parâmetro.

**Prefix-Tuning** (Li & Liang, 2021) preposiciona prefixos treináveis **em cada camada** do transformer (ativações, não só embeddings). Treinando ~**0,1% dos parâmetros** do modelo, obteve desempenho comparável ao fine-tuning completo em geração (table-to-text com GPT-2, sumarização com BART) — e melhor em regime de poucos dados e extrapolação para tópicos não vistos. **Prompt Tuning** (Lester et al., 2021) simplifica ao extremo: só embeddings **na entrada**, nada por camada. A descoberta central é o efeito da **escala**: em modelos pequenos fica bem atrás do fine-tuning, mas com T5-XXL (11B) **fecha o gap** — "the power of scale for parameter-efficient prompt tuning". Bônus operacional: um único modelo congelado serve N tarefas trocando só o soft prompt (~alguns KB por tarefa), e ensembles de prompts saem quase de graça.

O contraste com prompts discretos e legíveis define o trade-off: soft prompts são **mais potentes por parâmetro** (otimizam direto no contínuo, sem a restrição de cair em tokens reais), mas são **ilegíveis** (os vetores raramente correspondem a palavras próximas interpretáveis), **não portáveis** entre modelos e exigem **acesso aos internals** — inviáveis sobre APIs fechadas. Por isso a linha discreta ([APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md), [OPRO — LLM como otimizador](opro-llm-como-otimizador.md)) domina o mundo black-box, e os soft prompts vivem no mundo open-weights.

Historicamente, são o ramo contínuo da [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) e fundadores da área de **PEFT** (parameter-efficient fine-tuning), ao lado de adapters e LoRA. Conceitualmente, borram a fronteira entre [Engenharia de prompts](engenharia-de-prompts.md) e fine-tuning: condicionar pelo contexto e ajustar pesos são pontos do mesmo espectro de especialização — complementares ao [Instruction tuning](instruction-tuning.md) e ao [RLHF — RL a partir de feedback humano](rlhf.md), que moldam o modelo base sobre o qual qualquer prompt atua.

## Conexões
[Otimização automática de prompts](otimizacao-automatica-de-prompts.md) · [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) · [OPRO — LLM como otimizador](opro-llm-como-otimizador.md) · [Directional Stimulus Prompting](directional-stimulus-prompting.md) · [Instruction tuning](instruction-tuning.md) · [RLHF — RL a partir de feedback humano](rlhf.md) · [Engenharia de prompts](engenharia-de-prompts.md) · previsão do próximo token em transformers · [GraphPrompt — prompting em grafos](graphprompt.md)

## Fontes
[Prefix-Tuning: Optimizing Continuous Prompts for Generation](../fontes/li-liang-prefix-tuning.md) · [The Power of Scale for Parameter-Efficient Prompt Tuning](../fontes/lester-prompt-tuning.md)
