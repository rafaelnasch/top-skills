# Few-shot prompting

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Few-shot prompting** é incluir alguns exemplos resolvidos (input → output) no próprio prompt para que o modelo infira o padrão e o aplique ao caso novo — condicionamento por demonstração, sem atualizar nenhum peso. A técnica foi consagrada por Brown et al. (2020) em "Language Models are Few-Shot Learners": o GPT-3 (175B) mostrou que, com escala suficiente, demonstrações in-context substituem fine-tuning em muitas tarefas — o fenômeno batizado de [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md).

Boas práticas do Prompt Engineering Guide (DAIR.AI): mantenha **formato consistente** entre todos os exemplares (mesmos rótulos, mesmos separadores — o modelo aprende tanto o formato quanto a tarefa); use exemplos representativos da distribuição real dos inputs; e note o achado de Min et al. (2022): até **labels aleatórios** nos exemplares degradam pouco — o que carrega sinal é o espaço de labels, a distribuição dos inputs e o formato, mais do que a correção dos pares. A ordem dos exemplos também influencia ([O fim do prompt tem mais peso](fim-do-prompt-tem-mais-peso.md)).

A limitação clássica: few-shot **não resolve raciocínio multi-passo**. Em benchmarks como GSM8K (problemas matemáticos de escola), o GPT-3 com exemplares convencionais (só pergunta → resposta final) continuava falhando, mesmo com muitos exemplos — o modelo imita o formato da resposta, não o processo que chega até ela. Foi exatamente esse fracasso que motivou o [Chain-of-Thought (CoT)](chain-of-thought.md) (Wei et al., 2022): mudar os exemplares para mostrar os *passos intermediários*, não só a resposta.

Na escada da [Engenharia de prompts](engenharia-de-prompts.md): use [Zero-shot prompting](zero-shot-prompting.md) quando a instrução basta; few-shot quando precisa fixar formato, estilo ou tarefas fora do comum; CoT e além quando há raciocínio. Cada exemplar custa tokens de contexto — em produção, seleção dinâmica de exemplares (via embeddings, um primo de [RAG — Retrieval-Augmented Generation](rag.md)) é prática comum.

## Conexões
[Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) · [Zero-shot prompting](zero-shot-prompting.md) · [Chain-of-Thought (CoT)](chain-of-thought.md) · [Elementos de um prompt](elementos-de-um-prompt.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [O fim do prompt tem mais peso](fim-do-prompt-tem-mais-peso.md) · [Instruction tuning](instruction-tuning.md)

## Fontes
[Language Models are Few-Shot Learners](../fontes/brown-gpt3-few-shot-learners.md) · [Prompt Engineering Guide (DAIR.AI)](../fontes/prompt-engineering-guide-dair.md)
