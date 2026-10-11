# Large Language Models as Optimizers

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409).

Paper do OPRO — Optimization by PROmpting (Yang et al., 2023, DeepMind): usa o LLM como otimizador, alimentando um meta-prompt com a trajetória de soluções anteriores e seus scores pra gerar candidatos cada vez melhores. Na Tabela 1 do paper, a instrução otimizada alcançou 80,2% no GSM8K contra 71,8% de "Let's think step by step", diferença de 8,4 pontos percentuais. PaLM 2-L foi o modelo avaliador; PaLM 2-L-IT gerou essa instrução. Os resultados são específicos da configuração experimental. Descobriu o célebre "Take a deep breath and work on this problem step-by-step". Conceito relacionado: [OPRO — LLM como otimizador](../conceitos/opro-llm-como-otimizador.md).
