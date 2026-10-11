# Chain-of-Thought (CoT)

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Chain-of-Thought (CoT) prompting** é dar exemplares few-shot cujas respostas mostram os **passos intermediários de raciocínio** antes da resposta final — em vez de `pergunta → resposta`, o exemplar vira `pergunta → raciocínio passo a passo → resposta`. Proposto por Wei et al. (2022) em "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", resolveu o que o [Few-shot prompting](few-shot-prompting.md) convencional não resolvia: raciocínio aritmético, de senso comum e simbólico multi-passo.

O achado central: CoT é uma **habilidade emergente de escala** — só traz ganho em modelos grandes (na ordem de ~100B+ parâmetros); em modelos pequenos as cadeias geradas são fluentes porém ilógicas e a performance até piora. No auge do paper, **PaLM 540B com 8 exemplares CoT** atingiu o estado da arte no GSM8K, superando o SOTA anterior de um GPT-3 **fine-tuned com verificador** — prompting batendo fine-tuning em raciocínio matemático. A intuição mecânica: gerar os passos dá ao modelo "espaço de computação" serial em tokens, decompondo o problema em subpassos que o previsão do próximo token em transformers consegue acertar um de cada vez.

Bônus operacional: a cadeia gerada é **legível** — dá uma janela (imperfeita, não é garantia de fidelidade causal) para depurar *onde* o raciocínio quebrou, coisa que uma resposta seca não oferece.

A família cresceu rápido: [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) (Kojima et al., 2022) elimina os exemplares com "Let's think step by step"; **Auto-CoT** (Zhang et al., 2022) gera os exemplares automaticamente por clustering, evitando a curadoria manual; [Self-consistency](self-consistency.md) (Wang et al., 2022) amostra várias cadeias e vota; [Tree of Thoughts (ToT)](tree-of-thoughts.md) generaliza a cadeia para busca em árvore com backtracking; [Multimodal CoT](multimodal-cot.md) leva a técnica para visão+linguagem. CoT também é a espinha de técnicas agênticas como [ReAct prompting (Reason + Act)](react-prompting.md) e [Reflexion (reforço verbal)](reflexion.md) (ciclo de execução de agentes).

## Conexões
[Few-shot prompting](few-shot-prompting.md) · [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) · [Self-consistency](self-consistency.md) · [Tree of Thoughts (ToT)](tree-of-thoughts.md) · [Multimodal CoT](multimodal-cot.md) · [ReAct prompting (Reason + Act)](react-prompting.md) · [Reflexion (reforço verbal)](reflexion.md) · [PAL — Program-Aided Language Models](pal.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md)

## Fontes
[Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](../fontes/wei-chain-of-thought.md)
