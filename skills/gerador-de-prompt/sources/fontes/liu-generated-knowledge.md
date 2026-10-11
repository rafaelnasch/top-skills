# Generated Knowledge Prompting for Commonsense Reasoning

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Generated Knowledge Prompting for Commonsense Reasoning](https://arxiv.org/abs/2110.08387).

Liu et al. (UW/AI2, 2021, publicado na ACL 2022) propõem gerar conhecimento **do próprio LLM antes de responder**: primeiro o modelo produz statements de conhecimento relevantes à pergunta (via few-shot), depois esses statements são anexados ao prompt para a predição final. Sem retrieval externo nem knowledge base estruturada, melhora o state of the art em 4 benchmarks de commonsense (NumerSense, CommonsenseQA, CommonsenseQA 2.0, QASC). É o precursor "self-contained" do padrão que o [RAG — Retrieval-Augmented Generation](../conceitos/rag.md) resolve com retrieval externo. Conceito relacionado: [Generated knowledge prompting](../conceitos/generated-knowledge-prompting.md).
