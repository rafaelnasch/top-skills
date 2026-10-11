# Curse of Instructions

> Nota metodológica registrada em 2026-07-04. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

A **"Curse of Instructions"** é um achado de pesquisa (paper *Curse of Instructions*, Matsuo-Iwasawa Lab da Universidade de Tóquio) citado por Addy Osmani: **quanto mais instruções (ou dados) se empilham num único prompt, mais cai a aderência do modelo a cada uma delas**.

É o argumento central a favor de **specs modulares** em vez de um prompt monolítico. Osmani usa a "maldição" para defender quebrar a spec em pedaços e alimentar o agente com engenharia de contexto enxuto, em linha com a prática de escrita de specs boas.

O achado converge com a recomendação de Birgitta Böckeler e da Morph de selecionar contexto relevante e resumir documentos por níveis, em vez de incluir tudo numa única chamada. Também explica por que agentes **ignoram instruções complexas mesmo com janela de contexto grande**: capacidade de janela não é o mesmo que capacidade de obediência. Daí a preferência por delta e escopo pequeno (delta specs) e por marcar o que ainda falta em vez de sobrecarregar (pedido de esclarecimento).

## Conexões
especificações modulares · engenharia de contexto · Addy Osmani · pedido de esclarecimento

## Fontes
[How to write a good spec for AI agents — Addy Osmani](../fontes/osmani-how-to-write-good-spec.md)
