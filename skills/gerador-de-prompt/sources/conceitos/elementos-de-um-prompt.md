# Elementos de um prompt

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Um prompt bem construído combina até quatro elementos** — instrução, contexto, dados de entrada e indicador de saída — segundo a taxonomia do Prompt Engineering Guide (DAIR.AI). Nem todo prompt precisa dos quatro; o formato certo depende da tarefa.

Os quatro: (1) **Instrução** — a tarefa específica que o modelo deve executar ("classifique", "resuma", "traduza"); (2) **Contexto** — informação externa ou adicional que orienta a resposta (persona, regras, documentos — a semente do que vira engenharia de contexto e [RAG — Retrieval-Augmented Generation](rag.md) em escala); (3) **Dados de entrada** — o input concreto sobre o qual a tarefa opera; (4) **Indicador de saída** — o tipo ou formato da resposta esperada ("Sentimento:", JSON, tabela), que também funciona como âncora de parsing em [Prompt chaining (encadeamento de prompts)](prompt-chaining.md).

As dicas de design que acompanham a taxonomia: seja **específico e detalhado** (especificidade vence quase tudo, mas atenção à [Curse of Instructions](curse-of-instructions.md) — instruções demais degradam); **comece simples e itere** — [Engenharia de prompts](engenharia-de-prompts.md) é processo experimental, versione prompts como código ([Template mestre de prompt (12 seções)](template-mestre-de-prompt.md)); use separadores claros (como `###` ou XML) entre instrução e dados; e prefira dizer **o que fazer** em vez de "não faça X" — instruções negativas são mais fracas que afirmativas ("responda em no máximo 3 frases" > "não seja prolixo").

A posição dos elementos também importa: modelos tendem a dar mais peso ao que está no final da janela ([O fim do prompt tem mais peso](fim-do-prompt-tem-mais-peso.md)), então instruções críticas perto do fim e dados volumosos antes. Exemplos in-context ([Few-shot prompting](few-shot-prompting.md)) entram como um quinto elemento opcional — demonstrações do formato desejado, cujo mecanismo o [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) explica.

## Conexões
[Engenharia de prompts](engenharia-de-prompts.md) · [Configurações de inferência](configuracoes-de-inferencia.md) · [Zero-shot prompting](zero-shot-prompting.md) · [Few-shot prompting](few-shot-prompting.md) · [Template mestre de prompt (12 seções)](template-mestre-de-prompt.md) · [System prompt de produção](system-prompt-de-producao.md) · [Curse of Instructions](curse-of-instructions.md) · [O fim do prompt tem mais peso](fim-do-prompt-tem-mais-peso.md) · engenharia de contexto

## Fontes
[Prompt Engineering Guide (DAIR.AI)](../fontes/prompt-engineering-guide-dair.md)
