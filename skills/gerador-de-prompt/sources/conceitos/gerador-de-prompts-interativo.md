# Gerador de prompts interativo

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Gerador de prompts interativo** é um meta-prompt que, em vez de responder a tarefa, entrevista o usuário para depois *construir o prompt certo* para ela — elicitação de requisitos aplicada a [Engenharia de prompts](engenharia-de-prompts.md). É a versão manual e conversacional do que [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) e [OPRO — LLM como otimizador](opro-llm-como-otimizador.md) fazem por busca automática.

O template de criação interativa ([Criador de prompts interativo (template)](../templates/criador-de-prompts-interativo.md)) implementa isso em 6 passos: **coleta** (objetivo, tipo de output, contexto) → **identificação de necessidades** (tipo de tarefa, público-alvo, formato) → **seleção de técnica** numa biblioteca de 18 técnicas (de [Zero-shot prompting](zero-shot-prompting.md) a [RAG — Retrieval-Augmented Generation](rag.md), [ReAct prompting (Reason + Act)](react-prompting.md) e [Tree of Thoughts (ToT)](tree-of-thoughts.md)) → **criação do prompt personalizado** ([Elementos de um prompt](elementos-de-um-prompt.md)) → **revisão** (claro? específico? técnica adequada?) → **geração e avaliação** do output.

O insight estrutural: a escolha da técnica é uma *decisão de roteamento* que depende da natureza da tarefa — raciocínio pede [Chain-of-Thought (CoT)](chain-of-thought.md) ou [Self-consistency](self-consistency.md), conhecimento externo pede [RAG — Retrieval-Augmented Generation](rag.md), computação exata pede [PAL — Program-Aided Language Models](pal.md), tarefas compostas pedem [Prompt chaining (encadeamento de prompts)](prompt-chaining.md). Um gerador que pergunta antes de escolher encapsula esse conhecimento de roteamento para quem não domina o cardápio de técnicas.

A skill gerador-de-prompt aplica essa ideia nos modos CRIAR e ANALISAR. O [Template mestre de prompt (12 seções)](template-mestre-de-prompt.md) é a alternativa estática: uma estrutura fixa a preencher em vez de entrevista dinâmica.

## Conexões
[Engenharia de prompts](engenharia-de-prompts.md) · [Template mestre de prompt (12 seções)](template-mestre-de-prompt.md) · [Meta-prompting](meta-prompting.md) · [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) · [Elementos de um prompt](elementos-de-um-prompt.md) · [Prompt chaining (encadeamento de prompts)](prompt-chaining.md)

## Fontes
[Criador de prompts interativo (template)](../templates/criador-de-prompts-interativo.md)
