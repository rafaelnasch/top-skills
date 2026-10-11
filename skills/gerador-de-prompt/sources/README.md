# Fontes da skill gerador-de-prompt

Este pacote inclui notas de conceitos, fichas bibliográficas, um mapa de leitura e dois templates genéricos que fundamentam as referências operacionais em [`../references/`](../references/). As notas são sínteses metodológicas históricas das fontes indicadas; as datas originais de registro foram preservadas. Não houve reprodução de experimentos nem atualização científica nesta organização do material.

Os resultados de benchmarks pertencem aos modelos, tarefas e condições dos estudos citados. Eles não garantem o mesmo ganho em outros modelos ou aplicações. Use as referências operacionais para a execução e estes arquivos para consulta, estudo e ingestão conforme [`../INGEST.md`](../INGEST.md).

## Recorte e procedência

- **Conceitos:** sínteses curadas sobre técnicas de prompting e avaliação, relacionadas aos papers e à documentação citados.
- **Fontes:** fichas resumidas com autoria no texto e links públicos quando disponíveis. Não incluem textos integrais de papers, livros, cursos ou artigos de terceiros.
- **Templates:** dois modelos genéricos, sem identidade pessoal, links privados ou configuração de conta.
- **Prompts de produção:** somente uma ficha de contexto e sínteses metodológicas. A coleção específica não possui procedência pública estabelecida neste pacote; os prompts completos não são redistribuídos.
- **Heurística de posição do prompt:** atribuição bibliográfica preservada, sem redistribuir o curso de origem ou apresentar a heurística como lei universal.

## Índice

### Mapa de leitura (1)

- [Engenharia de Prompts (MOC)](mapas/engenharia-de-prompts-moc.md)

### Templates (2)

- [Criador de prompts interativo (template)](templates/criador-de-prompts-interativo.md)
- [Instrução-mestra de 12 seções (template)](templates/instrucao-mestra-12-secoes.md)

### Conceitos (35)

- [Active-Prompt](conceitos/active-prompt.md)
- [APE — Automatic Prompt Engineer](conceitos/ape-automatic-prompt-engineer.md)
- [Aprendizado em contexto (in-context learning)](conceitos/aprendizado-em-contexto.md)
- [ART — Automatic Reasoning and Tool-use](conceitos/art-automatic-reasoning-tool-use.md)
- [Auto-crítica de LLM](conceitos/auto-critica-de-llm.md)
- [Chain-of-Thought (CoT)](conceitos/chain-of-thought.md)
- [Configurações de inferência](conceitos/configuracoes-de-inferencia.md)
- [Curse of Instructions](conceitos/curse-of-instructions.md)
- [Directional Stimulus Prompting](conceitos/directional-stimulus-prompting.md)
- [Elementos de um prompt](conceitos/elementos-de-um-prompt.md)
- [Engenharia de prompts](conceitos/engenharia-de-prompts.md)
- [Few-shot prompting](conceitos/few-shot-prompting.md)
- [O fim do prompt tem mais peso](conceitos/fim-do-prompt-tem-mais-peso.md)
- [Generated knowledge prompting](conceitos/generated-knowledge-prompting.md)
- [Gerador de prompts interativo](conceitos/gerador-de-prompts-interativo.md)
- [GraphPrompt — prompting em grafos](conceitos/graphprompt.md)
- [Injeções de segurança em runtime](conceitos/injecoes-de-seguranca-runtime.md)
- [Instruction tuning](conceitos/instruction-tuning.md)
- [Meta-prompting](conceitos/meta-prompting.md)
- [Multimodal CoT](conceitos/multimodal-cot.md)
- [OPRO — LLM como otimizador](conceitos/opro-llm-como-otimizador.md)
- [Otimização automática de prompts](conceitos/otimizacao-automatica-de-prompts.md)
- [PAL — Program-Aided Language Models](conceitos/pal.md)
- [Prompt chaining (encadeamento de prompts)](conceitos/prompt-chaining.md)
- [RAG — Retrieval-Augmented Generation](conceitos/rag.md)
- [ReAct prompting (Reason + Act)](conceitos/react-prompting.md)
- [Reflexion (reforço verbal)](conceitos/reflexion.md)
- [RLHF — RL a partir de feedback humano](conceitos/rlhf.md)
- [Self-consistency](conceitos/self-consistency.md)
- [Soft prompts (prompts contínuos)](conceitos/soft-prompts.md)
- [System prompt de produção](conceitos/system-prompt-de-producao.md)
- [Template mestre de prompt (12 seções)](conceitos/template-mestre-de-prompt.md)
- [Tree of Thoughts (ToT)](conceitos/tree-of-thoughts.md)
- [Zero-shot CoT ("Let's think step by step")](conceitos/zero-shot-cot.md)
- [Zero-shot prompting](conceitos/zero-shot-prompting.md)

### Fichas de fontes (33)

- [AI-Driven Development — referência bibliográfica da trilha](fontes/ai-driven-development-formacao-dev.md)
- [Chain complex prompts for stronger performance (Anthropic)](fontes/anthropic-prompt-chaining-docs.md)
- [Language Models are Few-Shot Learners](fontes/brown-gpt3-few-shot-learners.md)
- [Deep Reinforcement Learning from Human Preferences](fontes/christiano-rl-human-preferences.md)
- [Padrões históricos descritos em prompts de produção](fontes/claude-system-prompts-producao.md)
- [Active Prompting with Chain-of-Thought for Large Language Models](fontes/diao-active-prompt.md)
- [Can LLMs Critique and Iterate on Their Own Outputs?](fontes/eric-jang-llm-self-critique.md)
- [PAL: Program-aided Language Models](fontes/gao-pal.md)
- [Retrieval-Augmented Generation for Large Language Models: A Survey](fontes/gao-rag-survey.md)
- [Language Is Not All You Need: Aligning Perception with Language Models](fontes/huang-kosmos-1.md)
- [Large Language Models are Zero-Shot Reasoners](fontes/kojima-zero-shot-reasoners.md)
- [The Power of Scale for Parameter-Efficient Prompt Tuning](fontes/lester-prompt-tuning.md)
- [Guiding Large Language Models via Directional Stimulus Prompting](fontes/li-directional-stimulus.md)
- [Prefix-Tuning: Optimizing Continuous Prompts for Generation](fontes/li-liang-prefix-tuning.md)
- [Generated Knowledge Prompting for Commonsense Reasoning](fontes/liu-generated-knowledge.md)
- [GraphPrompt: Unifying Pre-Training and Downstream Tasks for Graph Neural Networks](fontes/liu-graphprompt.md)
- [Large Language Model Guided Tree-of-Thought](fontes/long-tree-of-thought-guided.md)
- [Retrieval Augmented Generation: Streamlining the creation of intelligent NLP models](fontes/meta-ai-rag-blog.md)
- [Rethinking the Role of Demonstrations: What Makes In-Context Learning Work?](fontes/min-rethinking-demonstrations.md)
- [How to write a good spec for AI agents — Addy Osmani](fontes/osmani-how-to-write-good-spec.md)
- [ART: Automatic multi-step reasoning and tool-use for large language models](fontes/paranjape-art.md)
- [Prompt Engineering Guide (DAIR.AI)](fontes/prompt-engineering-guide-dair.md)
- [AutoPrompt: Eliciting Knowledge from Language Models with Automatically Generated Prompts](fontes/shin-autoprompt.md)
- [Reflexion: Language Agents with Verbal Reinforcement Learning](fontes/shinn-reflexion.md)
- [Query-Dependent Prompt Evaluation and Optimization with Offline Inverse RL](fontes/sun-prompt-oirl.md)
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models](fontes/wang-self-consistency.md)
- [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](fontes/wei-chain-of-thought.md)
- [Finetuned Language Models Are Zero-Shot Learners](fontes/wei-flan-zero-shot-learners.md)
- [Large Language Models as Optimizers](fontes/yang-opro.md)
- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](fontes/yao-tree-of-thoughts.md)
- [Meta Prompting for AI Systems](fontes/zhang-meta-prompting.md)
- [Multimodal Chain-of-Thought Reasoning in Language Models](fontes/zhang-multimodal-cot.md)
- [Large Language Models Are Human-Level Prompt Engineers](fontes/zhou-ape.md)

## Material novo

Para acrescentar uma fonte, mantenha somente material autorizado para compartilhamento, preserve atribuição e link público e siga [`../INGEST.md`](../INGEST.md). A presença em `sources/` não transforma o material em regra da skill: a destilação para `references/` exige revisão própria.
