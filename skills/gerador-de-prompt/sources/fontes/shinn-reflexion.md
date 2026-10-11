# Reflexion: Language Agents with Verbal Reinforcement Learning

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366).

Shinn et al. (Northeastern/MIT/Princeton, 2023) propõem **reforço verbal**: em vez de atualizar pesos, o agente reflete em linguagem natural sobre o feedback da tentativa anterior (Actor + Evaluator + Self-Reflection) e guarda essas reflexões numa memória episódica que orienta o próximo episódio. No HumanEval (código), atinge **91% pass@1 vs 80% do GPT-4** base; ganhos também em decision-making (AlfWorld) e reasoning (HotPotQA). Base do padrão auto-crítica/retry dos agentes modernos. Conceito relacionado: [Reflexion (reforço verbal)](../conceitos/reflexion.md) (ver também [Auto-crítica de LLM](../conceitos/auto-critica-de-llm.md)).
