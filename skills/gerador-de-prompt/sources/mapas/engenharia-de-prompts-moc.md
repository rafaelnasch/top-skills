# Engenharia de Prompts (MOC)

> Mapa metodológico registrado em 2026-07-05. Recorte histórico da bibliografia incluída.

Mapa metodológico de engenharia de prompts: fundamentos, técnicas de raciocínio, conhecimento e ferramentas externas, otimização, prompts de produção e templates reutilizáveis. As ligações deste recorte apontam para os conceitos e fichas incluídos no pacote.

## Fundamentos (por que prompting funciona)
- [Engenharia de prompts](../conceitos/engenharia-de-prompts.md) — A disciplina em si; nasce com o GPT-3 e explode com modelos instruídos.
- [Elementos de um prompt](../conceitos/elementos-de-um-prompt.md) — Instrução, contexto, dados de entrada, indicador de saída.
- [Configurações de inferência](../conceitos/configuracoes-de-inferencia.md) — Temperature, top-p, max tokens: o botão exatidão×criatividade.
- [Aprendizado em contexto (in-context learning)](../conceitos/aprendizado-em-contexto.md) — O modelo "aprende" da janela sem atualizar pesos; o que as demonstrações realmente fazem (Min et al.).
- [Instruction tuning](../conceitos/instruction-tuning.md) — FLAN: fine-tuning em instruções ensina o modelo a obedecer zero-shot.
- [RLHF — RL a partir de feedback humano](../conceitos/rlhf.md) — Preferências humanas → reward model: por que o modelo quer ajudar.

## Técnicas básicas
- [Zero-shot prompting](../conceitos/zero-shot-prompting.md) — Só a instrução; funciona graças a instruction tuning + RLHF.
- [Few-shot prompting](../conceitos/few-shot-prompting.md) — Exemplos in-context (GPT-3); falha em raciocínio complexo.

## Técnicas de raciocínio
- [Chain-of-Thought (CoT)](../conceitos/chain-of-thought.md) — Passos intermediários; habilidade emergente de escala (Wei et al. 2022).
- [Zero-shot CoT ("Let's think step by step")](../conceitos/zero-shot-cot.md) — "Let's think step by step" (Kojima et al. 2022).
- [Self-consistency](../conceitos/self-consistency.md) — Vários caminhos + voto majoritário (Wang et al. 2022).
- [Tree of Thoughts (ToT)](../conceitos/tree-of-thoughts.md) — Busca em árvore com avaliação e backtracking (Yao 2023; Long 2023).
- [Reflexion (reforço verbal)](../conceitos/reflexion.md) — Reforço verbal com memória episódica (Shinn et al. 2023).
- [Auto-crítica de LLM](../conceitos/auto-critica-de-llm.md) — Criticar é mais fácil que gerar (Eric Jang); base da auto-revisão.
- [Multimodal CoT](../conceitos/multimodal-cot.md) — CoT em dois estágios com visão+linguagem (Zhang et al. 2023).
- [Meta-prompting](../conceitos/meta-prompting.md) — Estrutura e sintaxe em vez de conteúdo (Zhang et al. 2023).

## Conhecimento e ferramentas externas
- [Generated knowledge prompting](../conceitos/generated-knowledge-prompting.md) — Gerar conhecimento antes de responder (Liu et al. 2021).
- [RAG — Retrieval-Augmented Generation](../conceitos/rag.md) — Recuperar antes de gerar; naive→advanced→modular (Lewis 2020; Gao 2023).
- [PAL — Program-Aided Language Models](../conceitos/pal.md) — Programa como raciocínio, interpretador como executor (Gao et al. 2022).
- [ReAct prompting (Reason + Act)](../conceitos/react-prompting.md) — Thought→Action→Observation; a semente do ciclo de execução de agentes (Yao et al. 2022).
- [ART — Automatic Reasoning and Tool-use](../conceitos/art-automatic-reasoning-tool-use.md) — Task library de raciocínio + tools (Paranjape et al. 2023).
- [Prompt chaining (encadeamento de prompts)](../conceitos/prompt-chaining.md) — Subtarefas encadeadas; recomendação Anthropic para prompts complexos.

## Otimização de prompts (o prompt como objeto otimizável)
- [Otimização automática de prompts](../conceitos/otimizacao-automatica-de-prompts.md) — A família: discreta vs contínua; avaliação vence intuição.
- [APE — Automatic Prompt Engineer](../conceitos/ape-automatic-prompt-engineer.md) — LLM gera e seleciona instruções (Zhou et al. 2022).
- [OPRO — LLM como otimizador](../conceitos/opro-llm-como-otimizador.md) — Meta-prompt com trajetória de scores (Yang et al. 2023).
- [Active-Prompt](../conceitos/active-prompt.md) — Anotar CoT onde a incerteza é maior (Diao et al. 2023).
- [Directional Stimulus Prompting](../conceitos/directional-stimulus-prompting.md) — Policy model pequeno gera hints via RL (Li et al. 2023).
- [Soft prompts (prompts contínuos)](../conceitos/soft-prompts.md) — Prefix-tuning e prompt tuning: prompts contínuos aprendidos.
- [GraphPrompt — prompting em grafos](../conceitos/graphprompt.md) — Prompting além de NLP: pre-training unificado em grafos.

## Prompts de produção (estudo de caso: Claude)
- [System prompt de produção](../conceitos/system-prompt-de-producao.md) — Anatomia real: blocos XML, categorias com exemplos, dezenas de milhares de tokens.
- [Injeções de segurança em runtime](../conceitos/injecoes-de-seguranca-runtime.md) — Classificador → injeção dinâmica: prompt como mecanismo de runtime.
- [O fim do prompt tem mais peso](../conceitos/fim-do-prompt-tem-mais-peso.md) — Onde colocar o que importa (nota pré-existente do cluster LLM).
- [Curse of Instructions](../conceitos/curse-of-instructions.md) — Por que empilhar instruções degrada (nota pré-existente).

## Templates genéricos
- [Gerador de prompts interativo](../conceitos/gerador-de-prompts-interativo.md) — Meta-prompt que entrevista antes de gerar (CRIADOR DE PROMPTS).
- [Template mestre de prompt (12 seções)](../conceitos/template-mestre-de-prompt.md) — 12 seções para instrução-mestra (ANÁLISE DE PROMPTS).
