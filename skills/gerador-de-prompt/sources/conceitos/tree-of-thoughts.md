# Tree of Thoughts (ToT)

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Tree of Thoughts (ToT)** generaliza o [Chain-of-Thought (CoT)](chain-of-thought.md) de uma cadeia linear para uma **busca em árvore de "thoughts"** — passos intermediários coerentes que o modelo gera, **avalia** e sobre os quais pode fazer **backtracking**. Proposto por Yao et al. (2023) em "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"; Long (2023) publicou de forma independente uma variante ("Tree-of-Thought") em que um **controlador treinado por RL** decide quando expandir, voltar atrás ou parar, em vez de heurísticas fixas de busca.

O framework tem quatro peças: (1) **decomposição** do problema em passos-thought; (2) **geração** de k candidatos por passo (amostragem ou propostas — [Configurações de inferência](configuracoes-de-inferencia.md) como motor); (3) **avaliação** de estados pelo próprio LLM (voto ou nota "sure/maybe/impossible" — parente direto da [Auto-crítica de LLM](auto-critica-de-llm.md)); (4) **algoritmo de busca** clássico — BFS ou DFS com poda — navegando a árvore. Onde o CoT commita com o primeiro caminho e a [Self-consistency](self-consistency.md) só vota no fim, o ToT delibera *durante* o processo, explorando alternativas e abandonando becos sem saída.

O número-símbolo do paper é o **Game of 24** (chegar a 24 com 4 números e operações aritméticas): GPT-4 com CoT resolve **4%**; com ToT, **74%**. Ganhos análogos em escrita criativa e mini-palavras-cruzadas. O custo acompanha: dezenas ou centenas de chamadas por problema — ToT é para problemas onde busca e planejamento justificam a conta, não para uso corriqueiro.

Existe uma versão-prompt simplificada, de Dave Hulbert: um único prompt no estilo *"imagine três especialistas respondendo a esta pergunta; cada um escreve um passo do seu raciocínio, compartilha com o grupo e, se perceber que errou, sai da discussão"* — uma emulação barata da árvore dentro de uma chamada só, sem busca real. Na fronteira agêntica, o espírito do ToT (gerar-avaliar-voltar) reaparece no ciclo de execução de agentes e em técnicas como [Reflexion (reforço verbal)](reflexion.md) e [ReAct prompting (Reason + Act)](react-prompting.md).

## Conexões
[Chain-of-Thought (CoT)](chain-of-thought.md) · [Self-consistency](self-consistency.md) · [Auto-crítica de LLM](auto-critica-de-llm.md) · [Reflexion (reforço verbal)](reflexion.md) · [ReAct prompting (Reason + Act)](react-prompting.md) · ciclo de execução de agentes · [Configurações de inferência](configuracoes-de-inferencia.md) · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](../fontes/yao-tree-of-thoughts.md) · [Large Language Model Guided Tree-of-Thought](../fontes/long-tree-of-thought-guided.md)
