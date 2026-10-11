# Configurações de inferência

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Configurações de inferência** são os parâmetros de amostragem que controlam *como* o modelo escolhe o próximo token — temperature, top-p, max tokens, stop sequences e as penalidades de frequência/presença. Junto com o prompt em si, são a segunda alavanca da [Engenharia de prompts](engenharia-de-prompts.md): o mesmo prompt produz saídas radicalmente diferentes sob parâmetros diferentes.

Os principais: **temperature** reescala a distribuição de probabilidade sobre o próximo token (previsão do próximo token em transformers) — baixa (~0) torna a saída quase determinística, alta achata a distribuição e favorece tokens improváveis; **top-p** (nucleus sampling) restringe a amostragem ao menor conjunto de tokens cuja probabilidade acumulada atinge p — a regra prática do guia da DAIR.AI é mexer em temperature *ou* top-p, não nos dois; **max tokens** limita o comprimento (e o custo) da resposta; **stop sequences** cortam a geração ao encontrar uma string — útil para forçar formato e delimitar etapas em [Prompt chaining (encadeamento de prompts)](prompt-chaining.md); **frequency penalty** penaliza tokens proporcionalmente à repetição, **presence penalty** penaliza igualmente qualquer token já usado — as duas combatem loops repetitivos.

O trade-off central é **exatidão × criatividade**: temperature baixa para tarefas factuais, extração e QA (respostas concisas e reproduzíveis); temperature alta para brainstorm, nomes, poesia. É a manifestação prática do determinismo e variabilidade — o LLM nunca é determinístico de verdade, mas os parâmetros regulam quanto da estocasticidade você deixa vazar.

Algumas técnicas dependem desses parâmetros como ingrediente ativo: [Self-consistency](self-consistency.md) exige temperature > 0 para amostrar múltiplos caminhos de raciocínio distintos antes do voto majoritário, e [Tree of Thoughts (ToT)](tree-of-thoughts.md) usa amostragem para gerar candidatos de "thoughts" a avaliar. Ou seja: o "defeito" (variância) vira mecanismo de busca.

## Conexões
[Engenharia de prompts](engenharia-de-prompts.md) · determinismo e variabilidade · previsão do próximo token em transformers · [Self-consistency](self-consistency.md) · [Tree of Thoughts (ToT)](tree-of-thoughts.md) · [Elementos de um prompt](elementos-de-um-prompt.md) · limitações de tokenização

## Fontes
[Prompt Engineering Guide (DAIR.AI)](../fontes/prompt-engineering-guide-dair.md)
