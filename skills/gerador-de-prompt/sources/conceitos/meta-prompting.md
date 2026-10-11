# Meta-prompting

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Meta-prompting** (Zhang et al., 2023) é prompting focado na **estrutura e sintaxe da tarefa** em vez do conteúdo específico: o prompt descreve o *formato* do raciocínio e da solução — um template abstrato — e não exemplares concretos preenchidos.

O exemplo do paper: em vez de dar ao modelo problemas resolvidos do dataset MATH ([Few-shot prompting](few-shot-prompting.md) clássico), dá-se o **template** de como um problema desse tipo se estrutura e como uma solução deve ser organizada ("Problema: [enunciado]. Solução: comece identificando..., derive passo a passo..., termine com a resposta em \boxed{}"). O modelo preenche a estrutura com o conteúdo do problema novo. É orientado a sintaxe, category-agnostic: o mesmo padrão estrutural serve a famílias inteiras de tarefas.

Duas vantagens práticas sobre few-shot: **eficiência de tokens** (um template é muito mais curto que k exemplares completos — sobra janela pro problema em si) e **comparação mais justa** entre modelos, porque na ausência de exemplares específicos a avaliação se aproxima do regime [Zero-shot prompting](zero-shot-prompting.md) — o desempenho não fica contaminado pela escolha (e sorte) dos exemplos. A aposta implícita: modelos pós [Instruction tuning](instruction-tuning.md) já sabem *o que* fazer; o que falta é dizer *em que forma*.

O termo também é usado num segundo sentido, ligado a este: **usar um LLM para gerar/refinar prompts** — um prompt sobre prompts. É o princípio do [Gerador de prompts interativo](gerador-de-prompts-interativo.md) e a ponte para a [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) ([APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md), [OPRO — LLM como otimizador](opro-llm-como-otimizador.md) — o meta-prompt do OPRO é literalmente um prompt que descreve como propor prompts melhores).

## Conexões
[Few-shot prompting](few-shot-prompting.md) · [Zero-shot prompting](zero-shot-prompting.md) · [Gerador de prompts interativo](gerador-de-prompts-interativo.md) · [Template mestre de prompt (12 seções)](template-mestre-de-prompt.md) · [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) · [OPRO — LLM como otimizador](opro-llm-como-otimizador.md) · [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) · [Instruction tuning](instruction-tuning.md) · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[Meta Prompting for AI Systems](../fontes/zhang-meta-prompting.md)
