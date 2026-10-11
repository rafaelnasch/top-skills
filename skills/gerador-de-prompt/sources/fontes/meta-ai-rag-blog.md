# Retrieval Augmented Generation: Streamlining the creation of intelligent NLP models

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Retrieval Augmented Generation: Streamlining the creation of intelligent NLP models](https://ai.meta.com/blog/retrieval-augmented-generation-streamlining-the-creation-of-intelligent-natural-language-processing-models/).

Post do blog da Meta AI que apresentou o RAG ao mundo (o paper é Lewis et al.
2020). A arquitetura combina **memória paramétrica** (o conhecimento nos pesos
de um seq2seq pré-treinado) com **memória não-paramétrica** — um índice denso
da Wikipedia consultado em tempo de geração. O ponto de venda: o conhecimento
fica **atualizável sem retreinar** o modelo — basta trocar o índice de
documentos. Conceito relacionado: [RAG — Retrieval-Augmented Generation](../conceitos/rag.md).
