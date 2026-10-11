# Zero-shot prompting

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Zero-shot prompting** é pedir a tarefa diretamente, sem nenhum exemplo no prompt — só a instrução e o input ("Classifique o sentimento: ..."). É o modo default de usar um LLM moderno e o degrau mais baixo da escada de técnicas da [Engenharia de prompts](engenharia-de-prompts.md).

Não funcionava bem nos modelos base: o GPT-3 puro (Brown et al., 2020) era muito melhor em [Few-shot prompting](few-shot-prompting.md) do que em zero-shot, porque um modelo treinado só em next-token prediction não "sabe" que deve obedecer instruções. O que mudou isso foi o [Instruction tuning](instruction-tuning.md): o FLAN (Wei et al., 2021) mostrou que fazer fine-tuning em dezenas de tarefas verbalizadas como instruções ensina o modelo a generalizar para instruções *não vistas* — o FLAN 137B superou o GPT-3 175B zero-shot na maioria das tarefas avaliadas. O [RLHF — RL a partir de feedback humano](rlhf.md) (Christiano et al., 2017; depois InstructGPT/ChatGPT) completou o alinhamento, ajustando o modelo à intenção humana. É por essa dupla que hoje "só pedir" funciona.

Quando o zero-shot falha, a escada sobe: adicione demonstrações ([Few-shot prompting](few-shot-prompting.md), via [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md)) para fixar formato e padrão; para tarefas de raciocínio multi-passo, use [Chain-of-Thought (CoT)](chain-of-thought.md) — ou o atalho híbrido do [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) (Kojima et al., 2022), que mantém o prompt sem exemplos mas destrava raciocínio com "Let's think step by step".

Regra prática: comece sempre em zero-shot (mais barato, menos tokens, sem viés de exemplares) e só escale quando a taxa de erro justificar. Instruções claras seguindo os [Elementos de um prompt](elementos-de-um-prompt.md) resolvem mais do que se imagina.

## Conexões
[Instruction tuning](instruction-tuning.md) · [RLHF — RL a partir de feedback humano](rlhf.md) · [Few-shot prompting](few-shot-prompting.md) · [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) · [Chain-of-Thought (CoT)](chain-of-thought.md) · [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) · [Elementos de um prompt](elementos-de-um-prompt.md) · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[Finetuned Language Models Are Zero-Shot Learners](../fontes/wei-flan-zero-shot-learners.md) · [Prompt Engineering Guide (DAIR.AI)](../fontes/prompt-engineering-guide-dair.md)
