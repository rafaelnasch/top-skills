# Multimodal CoT

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Multimodal CoT** estende o [Chain-of-Thought (CoT)](chain-of-thought.md) para entradas de **visão + linguagem**: o raciocínio passo a passo passa a ser condicionado também na imagem, não só no texto. Proposto por Zhang et al. (2023) em "Multimodal Chain-of-Thought Reasoning in Language Models".

O desenho é um framework em **dois estágios**, ambos consumindo texto e features visuais: (1) **geração de rationale** — o modelo produz a cadeia de raciocínio fundamentada nas duas modalidades; (2) **inferência da resposta** — o rationale gerado é anexado ao input original e o modelo responde. Separar os estágios ataca o problema central de modelos pequenos com CoT: a **alucinação de rationale** — cadeias fluentes porém descoladas da imagem, que contaminam a resposta. Com a fusão visual no primeiro estágio, o rationale nasce ancorado na evidência.

O resultado-símbolo: um modelo com **menos de 1B de parâmetros** (baseado em T5/UnifiedQA + features visuais) **superou o GPT-3.5 no ScienceQA** (benchmark de questões científicas com diagramas e imagens), passando também a baseline humana do dataset. A mensagem: para raciocínio multimodal, arquitetura do fluxo de raciocínio + fundamentação visual valem mais que escala bruta — um contraste interessante com a tese de emergência por escala do CoT original (Wei et al., 2022).

O contexto da época: o **Kosmos-1** (Huang et al., 2023, "Language Is Not All You Need") mostrava o caminho dos MLLMs nativos — um modelo único treinado de ponta a ponta em dados intercalados de texto e imagem, capaz de percepção, [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) multimodal e até QA visual sem OCR explícito. Multimodal CoT (composição de módulos + rationale explícito) e Kosmos-1 (multimodalidade nativa) são as duas rotas que convergiram nos modelos multimodais atuais, onde o CoT sobre imagens virou capacidade de prateleira.

## Conexões
[Chain-of-Thought (CoT)](chain-of-thought.md) · [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) · [Prompt chaining (encadeamento de prompts)](prompt-chaining.md) · [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) · [Auto-crítica de LLM](auto-critica-de-llm.md) · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[Multimodal Chain-of-Thought Reasoning in Language Models](../fontes/zhang-multimodal-cot.md) · [Language Is Not All You Need: Aligning Perception with Language Models](../fontes/huang-kosmos-1.md)
