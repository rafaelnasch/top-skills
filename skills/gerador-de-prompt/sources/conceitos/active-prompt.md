# Active-Prompt

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Active-Prompt** (Diao et al., 2023) responde à pergunta: dos milhares de exemplos possíveis, **quais vale a pena anotar com [Chain-of-Thought (CoT)](chain-of-thought.md) humano?** A técnica adapta os exemplares CoT à tarefa via seleção por incerteza, em vez de usar um conjunto fixo de exemplos escritos à mão (os mesmos 8 exemplares do paper original de CoT serviam pra tudo — dificilmente ótimos pra cada tarefa).

O algoritmo empresta o *uncertainty sampling* do active learning clássico: (1) para cada pergunta do pool, **amostra k respostas** do LLM (ex.: k=5) com os prompts atuais; (2) mede a **incerteza** pela discordância entre as k respostas (métricas como disagreement — quantas respostas distintas — ou entropia); (3) seleciona as perguntas **mais incertas**; (4) humanos anotam só essas com raciocínio CoT completo; (5) os novos exemplares anotados viram o prompt few-shot da tarefa.

A lógica econômica: anotação CoT humana é cara, então o orçamento deve ir pros exemplos onde o modelo mais patina — onde a demonstração ensina algo. Exemplos que o modelo já acerta com consistência não agregam informação. Com isso, Active-Prompt superou CoT com exemplares fixos e o CoT-auto em benchmarks de raciocínio aritmético, commonsense e simbólico.

Duas conexões estruturais: a medida de incerteza reusa a mecânica do [Self-consistency](self-consistency.md) (amostrar múltiplas cadeias e comparar respostas — lá pra *agregar*, aqui pra *diagnosticar*); e a técnica é meio-termo entre o [Few-shot prompting](few-shot-prompting.md) artesanal e a [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) plena — o humano ainda escreve o raciocínio, mas **a máquina escolhe onde** esse esforço rende mais.

## Conexões
[Chain-of-Thought (CoT)](chain-of-thought.md) · [Self-consistency](self-consistency.md) · [Few-shot prompting](few-shot-prompting.md) · [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) · [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md)

## Fontes
[Active Prompting with Chain-of-Thought for Large Language Models](../fontes/diao-active-prompt.md)
