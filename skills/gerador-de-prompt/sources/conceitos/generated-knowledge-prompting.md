# Generated knowledge prompting

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Generated knowledge prompting** (Liu et al., 2021) é gerar o conhecimento antes de responder: num primeiro passo, o modelo produz fatos/afirmações relevantes à pergunta; num segundo, esses enunciados são **incorporados ao prompt** e o modelo responde condicionado a eles.

A motivação é o *commonsense reasoning*: perguntas como "parte do golfe é tentar conseguir um total de pontos mais alto que os outros. Sim ou não?" derrubam o modelo direto, mas se antes ele gera o conhecimento ("no golfe vence quem tem a **menor** pontuação"), a resposta condicionada acerta. O conhecimento que o modelo "tem" nos pesos nem sempre é **ativado** pela pergunta — externalizá-lo como texto no contexto força a ativação. O paper mostrou ganhos em benchmarks como CommonsenseQA e NumerSense, com geração few-shot dos conhecimentos e integração por votação/pontuação das respostas.

É o **precursor conceitual do [RAG — Retrieval-Augmented Generation](rag.md) sem retrieval externo**: a mesma arquitetura recuperar-depois-gerar, só que a "base de conhecimento" é o próprio modelo (memória paramétrica em vez de não-paramétrica). A limitação é simétrica: o conhecimento gerado pode ser alucinado — não há fonte externa pra ancorar. Por isso o padrão evoluiu para RAG quando existe corpus confiável, mas continua útil quando não há índice nenhum. A mesma ideia reaparece em variações posteriores como o "recite-and-answer" (recitation-augmented generation).

Também é parente do [Chain-of-Thought (CoT)](chain-of-thought.md): ambos inserem texto intermediário gerado pelo próprio modelo entre pergunta e resposta. A diferença é o tipo — CoT gera *passos de raciocínio*; generated knowledge gera *fatos declarativos*. E é um argumento empírico central da [Engenharia de prompts](engenharia-de-prompts.md): o desempenho depende menos do que o modelo sabe e mais do que está **explícito no contexto** — a tese do engenharia de contexto.

## Conexões
[RAG — Retrieval-Augmented Generation](rag.md) · [Chain-of-Thought (CoT)](chain-of-thought.md) · engenharia de contexto · [Few-shot prompting](few-shot-prompting.md) · [Zero-shot prompting](zero-shot-prompting.md) · [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [Prompt chaining (encadeamento de prompts)](prompt-chaining.md)

## Fontes
[Generated Knowledge Prompting for Commonsense Reasoning](../fontes/liu-generated-knowledge.md)
