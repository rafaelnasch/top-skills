# OPRO — LLM como otimizador

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem reprodução dos experimentos. A comparação numérica abaixo foi conferida na Tabela 1 do paper.

**OPRO (Optimization by PROmpting)** (Yang et al., 2023, DeepMind — *Large Language Models as Optimizers*) usa o LLM como otimizador via **meta-prompt que contém a trajetória de otimização**: uma lista de pares (solução, score) já tentados, ordenados por score, mais a descrição da tarefa. A cada passo, o LLM lê a trajetória, **propõe a próxima instrução candidata**, ela é avaliada no modelo-alvo, e o par novo entra no meta-prompt. Repete até convergir.

A diferença para o [APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) é a memória: APE gera candidatos independentes e seleciona; OPRO mostra ao otimizador **o histórico do que funcionou e o quanto**, e o LLM extrai o padrão dos melhores para propor algo melhor — otimização iterativa em linguagem natural, sem gradiente, tratando o problema como um black-box. O paper valida a mecânica primeiro em problemas clássicos (regressão linear, TSP) antes de aplicá-la ao alvo real: a instrução do prompt.

O resultado-símbolo: no GSM8K com PaLM 2-L, OPRO encontrou **"Take a deep breath and work on this problem step-by-step"**, que atingiu ~80,2% de acurácia — **8,4 pontos percentuais** sobre "Let's think step by step" (~71,8%) e melhor ainda que o baseline sem instrução. "Respire fundo" melhorar matemática de um modelo é o tipo de descoberta contraintuitiva que nenhum humano proporia — e ilustra que o espaço de prompts é grande demais pra intuição. Detalhe importante: a instrução ótima é **específica do modelo** (a melhor pra PaLM não é a melhor pra GPT), minando a ideia de "frase mágica universal".

OPRO consolidou a família [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) e inspirou frameworks de otimização programática de pipelines de prompt. Sua premissa operacional é a mesma do APE: precisa de **métrica + conjunto de avaliação** — sem eval, não há trajetória a subir.

## Conexões
[APE — Automatic Prompt Engineer](ape-automatic-prompt-engineer.md) · [Otimização automática de prompts](otimizacao-automatica-de-prompts.md) · [Zero-shot CoT ("Let's think step by step")](zero-shot-cot.md) · [Meta-prompting](meta-prompting.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [Chain-of-Thought (CoT)](chain-of-thought.md) · [Configurações de inferência](configuracoes-de-inferencia.md)

## Fontes
[Large Language Models as Optimizers](../fontes/yang-opro.md)

Comparação consultada: [Tabela 1 — Large Language Models as Optimizers, v3](https://arxiv.org/html/2309.03409v3). PaLM 2-L é o avaliador; PaLM 2-L-IT é o otimizador associado à instrução citada.
