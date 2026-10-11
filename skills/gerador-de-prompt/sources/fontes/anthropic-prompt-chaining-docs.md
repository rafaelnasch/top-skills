# Chain complex prompts for stronger performance (Anthropic)

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Chain complex prompts for stronger performance (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-prompts).

Documentação oficial da Anthropic sobre quebrar tarefas complexas em prompts
encadeados, em vez de pedir tudo num prompt só. A tese: cada subtarefa recebe
a **atenção total** do modelo, o pipeline fica transparente (dá pra inspecionar
a saída de cada elo), o debugging é isolado por etapa, e dá pra montar
**self-correction chains** — um prompt que revisa/critica a saída do anterior.
Conceito relacionado: [Prompt chaining (encadeamento de prompts)](../conceitos/prompt-chaining.md).
