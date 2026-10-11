# Otimização automática de prompts

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Otimização automática de prompts** é a família de métodos que trata o prompt como **objeto otimizável** — uma variável a ser buscada, pontuada e melhorada por algoritmo — em vez de artefato artesanal escrito por intuição.

O eixo que organiza a família é **discreto vs contínuo**. Na linha **discreta**, o prompt continua sendo texto legível: o **AutoPrompt** (Shin et al., 2020) pioneirou com busca guiada por gradiente que preenche "trigger tokens" — eficaz, mas gerando prompts agramaticais e ilegíveis; o [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) (Zhou et al., 2022) trocou o gradiente por um LLM que propõe e seleciona instruções fluentes; o [OPRO — LLM como otimizador](opro-llm-como-otimizador.md) (Yang et al., 2023) adicionou a trajetória (solução, score) ao meta-prompt, fazendo o LLM subir a colina iterativamente; e o **Prompt-OIRL** (Sun et al., 2023) usa RL inverso **offline** para aprender um reward model a partir de dados de avaliação já existentes e escolher o melhor prompt **query-dependent** — por pergunta, não um prompt fixo por tarefa, e sem custo de inferência online.

Na linha **contínua**, abandona-se o texto: os [Soft prompts (prompts contínuos)](soft-prompts.md) (Prefix-Tuning, Prompt Tuning) otimizam vetores no espaço de embeddings por gradiente — mais potentes por parâmetro, porém ilegíveis e exigindo acesso aos internals do modelo. O [Directional Stimulus Prompting](directional-stimulus-prompting.md) fica no meio: hints discretos, mas aprendidos por RL com um policy model pequeno.

A implicação estratégica para a [Engenharia de prompts](engenharia-de-prompts.md): **o prompt artesanal tem teto**. APE e OPRO acharam frases que batem as dos humanos e que ninguém proporia por intuição ("Take a deep breath..."); a instrução ótima varia por modelo e por tarefa. Logo, a competência durável não é redigir o prompt perfeito — é montar **avaliação sistemática** (métrica + conjunto de teste) que permita buscar. Avaliação vence intuição; quem não mede, não otimiza.

## Conexões
[APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) · [OPRO — LLM como otimizador](opro-llm-como-otimizador.md) · [Soft prompts (prompts contínuos)](soft-prompts.md) · [Directional Stimulus Prompting](directional-stimulus-prompting.md) · [Active-Prompt](active-prompt.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [Meta-prompting](meta-prompting.md) · [Gerador de prompts interativo](gerador-de-prompts-interativo.md) · determinismo e variabilidade

## Fontes
[AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts](../fontes/shin-autoprompt.md) · [Large Language Models Are Human-Level Prompt Engineers](../fontes/zhou-ape.md) · [Large Language Models as Optimizers](../fontes/yang-opro.md) · [Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL](../fontes/sun-prompt-oirl.md)
