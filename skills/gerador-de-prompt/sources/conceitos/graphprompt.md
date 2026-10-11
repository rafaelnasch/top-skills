# GraphPrompt — prompting em grafos

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**GraphPrompt** (Liu et al., 2023 — WWW) leva o paradigma pre-train/prompt para **graph neural networks**: unifica o pré-treino e as tarefas downstream de grafos num **template comum baseado em subgrafos**, e adapta o modelo congelado a cada tarefa com um **prompt aprendível** — em vez de fine-tuning por tarefa.

O desenho: o pré-treino é auto-supervisionado por **link prediction** reformulado como similaridade entre subgrafos (nós conectados → subgrafos vizinhos parecidos). As tarefas downstream — classificação de nós e classificação de grafos — são **reformuladas no mesmo molde**: "de qual protótipo de classe este subgrafo está mais próximo?". Com pré-treino e downstream falando a mesma língua, o gap entre eles some, e o que resta a aprender é mínimo: um prompt — um vetor treinável que parametriza o **readout** (a agregação do subgrafo), destacando as dimensões que importam pra cada tarefa. É o análogo em grafos dos [Soft prompts (prompts contínuos)](soft-prompts.md) de NLP: modelo congelado, prompt contínuo por tarefa, forte em few-shot.

O ponto que interessa além dos GNNs: **"prompting" como paradigma extrapola o NLP**. A receita — pré-treinar genérico, congelar, reformular a tarefa downstream no formato do pré-treino, adaptar por um prompt leve — funciona onde houver um modelo fundacional e tarefas variadas: texto, grafos, visão (VPT), multimodal. Prompting deixa de ser "escrever instruções em inglês" e revela sua forma geral: **condicionar um modelo congelado com um sinal pequeno, barato e específico da tarefa** em vez de reajustar pesos.

Pra [Engenharia de prompts](engenharia-de-prompts.md), é o lembrete de que o prompt é um conceito de *interface com modelos pré-treinados*, não um truque de chatbot — a versão em linguagem natural ([Zero-shot prompting](zero-shot-prompting.md), [Few-shot prompting](few-shot-prompting.md)) é o caso particular mais visível de um padrão que a literatura de [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) e soft prompts explora em toda a sua generalidade.

## Conexões
[Soft prompts (prompts contínuos)](soft-prompts.md) · [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [Instruction tuning](instruction-tuning.md) · [Zero-shot prompting](zero-shot-prompting.md) · [Few-shot prompting](few-shot-prompting.md) · [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md)

## Fontes
[GraphPrompt: Unifying Pre-Training and Downstream Tasks for Graph Neural Networks](../fontes/liu-graphprompt.md)
