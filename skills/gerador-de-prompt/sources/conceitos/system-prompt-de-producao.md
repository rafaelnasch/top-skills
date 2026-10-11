# System prompt de produção

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**System prompt de produção** é a instrução de sistema de um produto de IA em operação. Esta nota registra padrões descritos por uma coleção histórica de prompts extraídos e estudados: blocos estruturados, exemplos, regras condicionais e casos-limite. A coleção é uma referência metodológica para [Engenharia de prompts](engenharia-de-prompts.md), sem confirmação do comportamento atual de um produto.

A anatomia é feita de **blocos XML-tagged**: `<citation_instructions>`, `<artifacts_info>`, `<search_instructions>`, `<userPreferences>`, `<userStyle>`. A tag XML é a unidade de organização — cada bloco é um domínio de comportamento isolado, endereçável e substituível, o mesmo princípio de modularidade que um instruções de projeto (CLAUDE.md e AGENTS.md) bem escrito usa.

O comportamento é condicionado por **categorias explícitas com exemplos**. As `search_instructions` do claude.ai, por exemplo, definem uma escala de complexidade — *nunca buscar* (fato estável), *oferecer busca*, *busca única*, *research* com escala de tool calls conforme a dificuldade — e cada categoria vem com exemplos concretos de queries. Exemplos valem mais que regras abstratas: em vez de "busque quando necessário", o prompt mostra caso a caso o que cai onde — na prática, [Few-shot prompting](few-shot-prompting.md) embutido no system prompt.

Outros padrões recorrentes: **regras de formato por ambiente** (no CLI, respostas ≤4 linhas — o formato é função do contexto de exibição, não do conteúdo); **persona e guardrails no fim** do prompt, aproveitando que o [O fim do prompt tem mais peso](fim-do-prompt-tem-mais-peso.md); e **instruções positivas** ("faça Y") em vez de negativas ("não faça X"), que dão ao modelo um alvo em vez de um buraco.

As lições consolidadas: produção = prompts **LONGOS, estruturados, cheios de exemplos e casos-limite** — o oposto do mito do prompt curto mágico. Quem escreve um [Template mestre de prompt (12 seções)](template-mestre-de-prompt.md) ou pratica engenharia de contexto deveria estudar esses artefatos como um arquiteto estuda prédios construídos, com atenção aos limites (a [Curse of Instructions](curse-of-instructions.md) cobra seu preço: quanto mais regras, menor a aderência a cada uma — daí a importância de blocos bem separados e exemplos). E o prompt de design-time não é a única camada: em runtime entram as [Injeções de segurança em runtime](injecoes-de-seguranca-runtime.md).

## Conexões
[Engenharia de prompts](engenharia-de-prompts.md) · instruções de projeto (CLAUDE.md e AGENTS.md) · engenharia de contexto · [Curse of Instructions](curse-of-instructions.md) · [Template mestre de prompt (12 seções)](template-mestre-de-prompt.md) · [Injeções de segurança em runtime](injecoes-de-seguranca-runtime.md) · [Few-shot prompting](few-shot-prompting.md) · [O fim do prompt tem mais peso](fim-do-prompt-tem-mais-peso.md)

## Fontes
[System prompts de produção do Claude (coleção extraída)](../fontes/claude-system-prompts-producao.md)
