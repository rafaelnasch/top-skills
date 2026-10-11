# Aprendizado em contexto (in-context learning)

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Aprendizado em contexto** (in-context learning, ICL) é a capacidade de um LLM "aprender" uma tarefa apenas a partir do que está na janela de contexto — demonstrações, instruções, padrões — **sem atualizar nenhum peso**. Toda a adaptação acontece no forward pass: o modelo condiciona a geração do próximo token ao padrão presente no prompt (previsão do próximo token em transformers, viabilizado pela atenção — mecanismo de atenção).

O fenômeno emergiu **com escala**: Brown et al. (2020) mostraram no GPT-3 que a performance few-shot cresce de forma acentuada com o tamanho do modelo — modelos pequenos quase não se beneficiam de demonstrações, o 175B extrai muito delas. É o mecanismo que sustenta o [Few-shot prompting](few-shot-prompting.md) e, indiretamente, tudo que a [Engenharia de prompts](engenharia-de-prompts.md) faz: um prompt é, no fundo, uma tentativa de programar o ICL.

O achado contraintuitivo é de Min et al. (2022), "Rethinking the Role of Demonstrations": substituir os labels corretos dos exemplares por **labels aleatórios quase não degrada** a performance. O que realmente importa nas demonstrações são três coisas: (1) o **espaço de labels** exposto (quais respostas são possíveis), (2) a **distribuição dos inputs** (que tipo de texto entra) e (3) o **formato** da sequência (como input e label se encaixam). Ou seja: as demonstrações menos *ensinam* o mapeamento input→label e mais *ativam e localizam* capacidades que o modelo já tem do pré-treino.

Implicação prática: capriche em formato, cobertura do espaço de saída e representatividade dos inputs antes de se preocupar com a perfeição de cada par. E implicação conceitual: o ICL é a base do programação por contexto — programar por contexto em vez de por código — e o que o engenharia de contexto leva ao limite: se o modelo aprende do que vê, curar o que ele vê é a engenharia.

## Conexões
[Few-shot prompting](few-shot-prompting.md) · [Zero-shot prompting](zero-shot-prompting.md) · [Chain-of-Thought (CoT)](chain-of-thought.md) · mecanismo de atenção · previsão do próximo token em transformers · engenharia de contexto · programação por contexto · [Soft prompts (prompts contínuos)](soft-prompts.md)

## Fontes
[Language Models are Few-Shot Learners](../fontes/brown-gpt3-few-shot-learners.md) · [Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?](../fontes/min-rethinking-demonstrations.md)
