# APE — Automatic Prompt Engineer

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**APE (Automatic Prompt Engineer)** (Zhou et al., 2022) trata a criação de instruções como **busca automática**: um LLM gera candidatos de instrução a partir de exemplos entrada→saída da tarefa, cada candidato é executado no modelo-alvo, e vence o que maximiza o score numa métrica de avaliação. O subtítulo do paper virou slogan: *"Large language models are human-level prompt engineers"* — as instruções encontradas igualaram ou superaram as escritas por humanos na maioria das 24 tarefas de instruction induction avaliadas.

O pipeline: (1) **propor** — um LLM infere instruções plausíveis dado um punhado de demonstrações ("a instrução era ___"); (2) **avaliar** — cada candidata roda no modelo-alvo sobre um conjunto de validação e recebe score (acurácia / log-prob); (3) opcionalmente **refinar** — gerar variações semânticas das melhores (busca de Monte Carlo iterativa) e reavaliar. É a estrutura clássica propor-avaliar-selecionar, com LLMs nos dois papéis.

O resultado mais citado: APE descobriu **"Let's work this out in a step by step way to be sure we have the right answer"**, que superou o clássico "Let's think step by step" do [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) (Kojima et al., 2022) em avaliações descritas pelo estudo. Uma frase achada por busca automática bateu a frase-ícone achada por humanos: ninguém teria chegado nela por intuição, e é exatamente esse o argumento.

APE fundou a linha da [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) discreta, depois estendida pelo [OPRO — LLM como otimizador](opro-llm-como-otimizador.md) (que adiciona a trajetória de otimização ao meta-prompt). A lição prática pra [Engenharia de prompts](engenharia-de-prompts.md): prompt artesanal tem teto — com uma métrica e um conjunto de validação, **busca sistemática vence intuição**. O que pressupõe o mais difícil: ter avaliação automatizável.

## Conexões
[Otimização automática de prompts](otimizacao-automatica-de-prompts.md) · [OPRO — LLM como otimizador](opro-llm-como-otimizador.md) · [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) · [Meta-prompting](meta-prompting.md) · [Gerador de prompts interativo](gerador-de-prompts-interativo.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) · [Chain-of-Thought (CoT)](chain-of-thought.md)

## Fontes
[Large Language Models Are Human-Level Prompt Engineers](../fontes/zhou-ape.md)
