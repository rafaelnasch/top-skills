# Zero-shot CoT ("Let's think step by step")

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Zero-shot CoT** é destravar raciocínio passo a passo **sem nenhum exemplar**: basta anexar "Let's think step by step" após a pergunta. Kojima et al. (2022), em "Large Language Models are Zero-Shot Reasoners", mostraram que essa única frase-gatilho transforma LLMs em raciocinadores zero-shot decentes — o meio-termo entre [Zero-shot prompting](zero-shot-prompting.md) puro e o [Chain-of-Thought (CoT)](chain-of-thought.md) few-shot de Wei et al.

O método tem **dois passos de prompting**: (1) **extração de raciocínio** — envia a pergunta + "Let's think step by step" e o modelo gera a cadeia; (2) **extração de resposta** — reenvia pergunta + cadeia gerada + um indicador como "Therefore, the answer is" para colher a resposta final em formato parseável. É um mini [Prompt chaining (encadeamento de prompts)](prompt-chaining.md) de duas chamadas, resolvendo o problema de a cadeia livre não terminar num formato extraível.

Os números do paper (com InstructGPT, text-davinci-002): **MultiArith saltou de 17,7% para 78,7%** e GSM8K de 10,4% para 40,7% — só pela frase-gatilho. Como o CoT com exemplares, o efeito é dependente de escala e aparece com força em modelos grandes e instruídos ([Instruction tuning](instruction-tuning.md) + [RLHF — RL a partir de feedback humano](rlhf.md) ajudam o modelo a obedecer o gatilho). Kojima et al. testaram variações da frase; "Let's think step by step" venceu as alternativas — e trabalhos posteriores de [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) (como [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md), que achou "Let's work this out in a step by step way to be sure we have the right answer") mostraram que dá para otimizar até o gatilho.

Uso prático: é o upgrade mais barato da [Engenharia de prompts](engenharia-de-prompts.md) — zero exemplares, zero curadoria — ideal quando não há exemplos disponíveis. Quando a tarefa é crítica, combine com [Self-consistency](self-consistency.md) (várias cadeias + voto) ou suba para CoT few-shot com exemplares de qualidade.

## Conexões
[Chain-of-Thought (CoT)](chain-of-thought.md) · [Zero-shot prompting](zero-shot-prompting.md) · [Self-consistency](self-consistency.md) · [Prompt chaining (encadeamento de prompts)](prompt-chaining.md) · [Instruction tuning](instruction-tuning.md) · [RLHF — RL a partir de feedback humano](rlhf.md) · [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[Large Language Models are Zero-Shot Reasoners](../fontes/kojima-zero-shot-reasoners.md)
