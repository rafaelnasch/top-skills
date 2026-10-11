# Instruction tuning

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Instruction tuning** é fazer fine-tuning de um LLM numa **mistura de muitas tarefas verbalizadas como instruções em linguagem natural** — de modo que o modelo aprenda a *seguir instruções em geral*, melhorando o desempenho zero-shot em tarefas que ele **nunca viu**. O trabalho canônico é o **FLAN** (Wei et al., 2021, "Finetuned Language Models are Zero-Shot Learners"): um LaMDA-PT de 137B afinado em ~60 datasets de NLP reescritos como instruções (via templates múltiplos por tarefa).

O protocolo de avaliação é o ponto: as tarefas são agrupadas em clusters (tradução, NLI, QA, sumarização...) e o modelo é avaliado num cluster **excluído do treino** — medindo generalização de instrução, não memorização de tarefa. Resultado: o FLAN superou o **GPT-3 175B zero-shot na maioria dos benchmarks avaliados** (e até o GPT-3 few-shot em vários), sendo mais barato em parâmetros. Achados colaterais: o ganho **cresce com o número de clusters** de tarefas no treino e — eco do [Chain-of-Thought (CoT)](chain-of-thought.md) — **só aparece em escala suficiente**; em modelos pequenos, o instruction tuning chegou a piorar a generalização.

É o fundamento de por que o [Zero-shot prompting](zero-shot-prompting.md) funciona: um modelo base só completa texto (previsão do próximo token em transformers); um modelo instruído mapeia "instrução → comportamento". Forma par com o [RLHF — RL a partir de feedback humano](rlhf.md) (Christiano et al., 2017; InstructGPT): o instruction tuning ensina o **formato** de seguir instruções por imitação supervisionada; o RLHF calibra o comportamento pela **preferência humana**. A dupla (SFT + RLHF) é a receita que transformou modelos base em assistentes — e que tornou a [Engenharia de prompts](engenharia-de-prompts.md) acessível: escrever instruções claras só funciona porque o modelo foi treinado para honrá-las.

Consequências práticas: modelos instruídos respondem melhor a instruções explícitas e formatos de prompt semelhantes aos templates de treino ([Elementos de um prompt](elementos-de-um-prompt.md)); gatilhos como o do [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) funcionam melhor em modelos instruídos; e a sensibilidade a instruções tem seu lado B — instruções demais competem entre si ([Curse of Instructions](curse-of-instructions.md)).

## Conexões
[Zero-shot prompting](zero-shot-prompting.md) · [RLHF — RL a partir de feedback humano](rlhf.md) · [Few-shot prompting](few-shot-prompting.md) · [Chain-of-Thought (CoT)](chain-of-thought.md) · [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) · [Elementos de um prompt](elementos-de-um-prompt.md) · [Curse of Instructions](curse-of-instructions.md) · previsão do próximo token em transformers · [Soft prompts (prompts contínuos)](soft-prompts.md)

## Fontes
[Finetuned Language Models Are Zero-Shot Learners](../fontes/wei-flan-zero-shot-learners.md)
