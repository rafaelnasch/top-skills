# Auto-crítica de LLM

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Auto-crítica de LLM** é o padrão de fazer o modelo **criticar e iterar sobre as próprias saídas**: gera, avalia o que gerou, corrige, repete. Eric Jang (2023) popularizou a observação-base em "Can LLMs Critique and Iterate on Their Own Outputs?": para muitas tarefas, **criticar é mais fácil que gerar** — verificar uma solução exige menos "computação" que produzi-la (a mesma assimetria de P vs NP, ou de reconhecer boa escrita vs escrever bem). Se o modelo consegue detectar defeito na própria resposta, um segundo passe barato colhe qualidade que o primeiro deixou na mesa.

O padrão mínimo é um [Prompt chaining (encadeamento de prompts)](prompt-chaining.md) de dois papéis: prompt gerador → prompt crítico ("aponte erros, omissões, violações de requisito") → prompt revisor que reescreve incorporando a crítica. Variações: rubricas explícitas, crítico com persona distinta, N críticas agregadas. É o mecanismo interno do avaliador de estados no [Tree of Thoughts (ToT)](tree-of-thoughts.md) e, em versão estatística, da [Self-consistency](self-consistency.md) — onde a "crítica" emerge da concordância entre amostras em vez de um juízo explícito.

O limite, que o próprio Jang e a literatura posterior sublinham: **autocrítica nem sempre melhora**. Sem **sinal externo de verdade**, o modelo pode "corrigir" respostas certas para erradas, confabular defeitos ou aprovar erros que ele mesmo cometeu — os vieses da geração contaminam a crítica, porque é o mesmo modelo dos dois lados. A autocrítica morde de verdade quando há verificador objetivo no loop: testes unitários, execução de código ([PAL — Program-Aided Language Models](pal.md)), busca externa ([RAG — Retrieval-Augmented Generation](rag.md), [ReAct prompting (Reason + Act)](react-prompting.md)), regras checáveis.

É a ponte conceitual para [Reflexion (reforço verbal)](reflexion.md) (Shinn et al., 2023), que estrutura a autocrítica em Actor/Evaluator/Self-Reflection com memória episódica e avaliador externo — e para o design de harness de agentes (estrutura de execução de agentes): não confie no modelo se auto-aprovar; dê a ele ferramentas de verificação e faça a crítica ser ancorada em evidência.

## Revisão por um avaliador distinto

Um avaliador distinto pode reduzir a correlação entre os vieses de geração e revisão. Isso continua sendo uma medida parcial: trocar o modelo que revisa não substitui testes, fontes ou outro sinal externo de verdade.

## Conexões
[Reflexion (reforço verbal)](reflexion.md) · [Self-consistency](self-consistency.md) · [Tree of Thoughts (ToT)](tree-of-thoughts.md) · [Prompt chaining (encadeamento de prompts)](prompt-chaining.md) · [ReAct prompting (Reason + Act)](react-prompting.md) · [PAL — Program-Aided Language Models](pal.md) · [RAG — Retrieval-Augmented Generation](rag.md) · estrutura de execução de agentes · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[Can LLMs Critique and Iterate on Their Own Outputs?](../fontes/eric-jang-llm-self-critique.md)
