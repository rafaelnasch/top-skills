# Self-consistency

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Self-consistency** é substituir o greedy decoding do [Chain-of-Thought (CoT)](chain-of-thought.md) por **amostragem de múltiplos caminhos de raciocínio** (temperature > 0) e escolher a resposta final por **voto majoritário** sobre as respostas — a mais consistente entre as cadeias vence. Proposta por Wang et al. (2022) em "Self-Consistency Improves Chain of Thought Reasoning in Language Models".

A intuição: problemas de raciocínio complexos admitem **vários caminhos válidos até a mesma resposta correta**, enquanto caminhos errados tendem a divergir entre si. Amostrar N cadeias (tipicamente dezenas) e marginalizar sobre os raciocínios — ignorando *como* cada um chegou lá e agregando só o *onde* chegou — filtra o erro idiossincrático de uma cadeia única. É um ensemble de um modelo só, sem treino extra, explorando a estocasticidade das [Configurações de inferência](configuracoes-de-inferencia.md) como mecanismo de busca (determinismo e variabilidade).

Os ganhos do paper sobre CoT com greedy decoding foram grandes e consistentes entre modelos (GPT-3, LaMDA, PaLM): **GSM8K +17,9%**, SVAMP +11,0%, AQuA +12,2%, entre outros benchmarks de raciocínio aritmético e de senso comum. Funciona melhor exatamente onde o CoT já funciona (modelos grandes, tarefas com resposta final verificável/comparável) e o ganho cresce com o número de amostras até saturar.

O custo é o trade-off óbvio: N cadeias = N vezes o custo de inferência. Por isso, na escada da [Engenharia de prompts](engenharia-de-prompts.md), self-consistency é o passo entre o CoT simples e buscas mais estruturadas: quando voto simples não basta e o problema exige explorar, avaliar e voltar atrás, o próximo degrau é [Tree of Thoughts (ToT)](tree-of-thoughts.md). Também dialoga com [Auto-crítica de LLM](auto-critica-de-llm.md) — em vez de o modelo criticar a própria saída, a "crítica" emerge estatisticamente da concordância entre amostras — e com [Reflexion (reforço verbal)](reflexion.md), que itera com feedback verbal em vez de votar.

## Conexões
[Chain-of-Thought (CoT)](chain-of-thought.md) · [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) · [Tree of Thoughts (ToT)](tree-of-thoughts.md) · [Configurações de inferência](configuracoes-de-inferencia.md) · determinismo e variabilidade · [Auto-crítica de LLM](auto-critica-de-llm.md) · [Reflexion (reforço verbal)](reflexion.md) · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[Self-Consistency Improves Chain of Thought Reasoning in Language Models](../fontes/wang-self-consistency.md)
