# RAG — Retrieval-Augmented Generation

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**RAG (Retrieval-Augmented Generation)** é condicionar a geração do LLM a conhecimento recuperado de uma base externa no momento da pergunta: um retriever busca os documentos relevantes, eles entram no prompt, e o modelo responde ancorado neles. Proposto por Lewis et al. (2020, Meta AI) combinando um retriever denso (DPR) com um gerador seq2seq (BART) sobre a Wikipedia.

O contraste central é **memória paramétrica vs não-paramétrica**: o que o modelo "sabe" nos pesos é caro de atualizar, congela no cutoff de treino e alucina; a memória não-paramétrica (o índice de documentos) é **trocável sem retreinar** — basta reindexar. Por isso RAG ataca de uma vez os dois males clássicos: alucinação e conhecimento desatualizado, e ainda dá **citabilidade** (a resposta aponta pra fonte).

O survey de Gao et al. (2023) organiza a evolução em três estágios: **naive RAG** (indexa → recupera → gera, o pipeline ingênuo), **advanced RAG** (otimizações pré-retrieval como reescrita de query e pós-retrieval como reranking e compressão de contexto) e **modular RAG** (módulos rearranjáveis — busca, memória, roteamento, fusão — incluindo padrões iterativos e adaptativos onde o modelo decide quando recuperar). Na prática, a fronteira entre RAG modular e agente com tool de busca (via [ReAct prompting (Reason + Act)](react-prompting.md)) fica borrada.

RAG é, no fundo, um caso especial de engenharia de contexto: curar o que entra na janela de contexto. O precursor sem retrieval externo é o [Generated knowledge prompting](generated-knowledge-prompting.md) (o próprio modelo gera o "documento"); e um vault como o biblioteca de notas para recuperação de conhecimento é uma base de conhecimento desenhada pra esse padrão — notas atômicas e linkadas são unidades de retrieval ideais.

## Conexões
engenharia de contexto · [Generated knowledge prompting](generated-knowledge-prompting.md) · [ReAct prompting (Reason + Act)](react-prompting.md) · biblioteca de notas para recuperação de conhecimento · [Few-shot prompting](few-shot-prompting.md) · [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [O fim do prompt tem mais peso](fim-do-prompt-tem-mais-peso.md)

## Fontes
[Retrieval-Augmented Generation for Large Language Models: A Survey](../fontes/gao-rag-survey.md) · [Retrieval Augmented Generation: Streamlining the creation of intelligent NLP models](../fontes/meta-ai-rag-blog.md)
