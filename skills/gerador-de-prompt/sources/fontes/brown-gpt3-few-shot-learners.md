# Language Models are Few-Shot Learners

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165).

Paper do GPT-3 (Brown et al., 2020): um LM autoregressivo de 175B de parâmetros que executa tarefas novas só com instruções e exemplos no prompt, sem gradient updates nem fine-tuning. Demonstrou que escala destrava in-context learning — desempenho competitivo em tradução, QA e cloze em regimes zero-shot, one-shot e few-shot. É o paper que fundou o prompting moderno: a tarefa passa a ser especificada em linguagem natural no contexto. Conceito relacionado: [Few-shot prompting](../conceitos/few-shot-prompting.md), [Aprendizado em contexto (in-context learning)](../conceitos/aprendizado-em-contexto.md).
