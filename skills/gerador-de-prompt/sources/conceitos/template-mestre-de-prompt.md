# Template mestre de prompt (12 seções)

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Template mestre de prompt** é uma estrutura fixa de seções para escrever mensagens de sistema completas — em vez de improvisar cada prompt, preenche-se um esqueleto que já força as decisões importantes. O template de instrução-mestra ([Instrução-mestra de 12 seções (template)](../templates/instrucao-mestra-12-secoes.md)) tem 12 seções: objetivo & contexto, papel & âmbito, estilo & tom, ferramentas/fontes/citações, artefatos, memória & preferências, entradas, saída esperada, processo passo a passo, checklist de qualidade, diretrizes específicas e limitações & recusas — mais um bloco de execução por chamada.

A anatomia espelha em miniatura um [System prompt de produção](system-prompt-de-producao.md): papel e escopo primeiro, política de ferramentas explícita, regras de formato por ambiente (CLI ≤ 4 linhas), guardrails de recusa e separação entre instrução-mestra (estável) e bloco de execução (variável por tarefa). É o mesmo padrão instrução/dados que os [Elementos de um prompt](elementos-de-um-prompt.md) descrevem, escalado para prompts longos.

Dois mecanismos do template valem destacar: a **especificação da saída** (§8 — estrutura, campos obrigatórios, critérios de qualidade) transforma o prompt num contrato verificável, eco do espírito de testes como contrato; e a **checklist de auto-revisão** (§10) embute [Auto-crítica de LLM](auto-critica-de-llm.md) no próprio fluxo — o modelo confere as exigências antes de entregar. A cláusula final ("se faltar informação crítica, liste exatamente o que precisa e pare") é um guardrail contra alucinação de premissas, aparentado do pedido de esclarecimento do mundo SDD.

Contraste com o [Gerador de prompts interativo](gerador-de-prompts-interativo.md): o template é estático (preencher lacunas), o gerador é dinâmico (entrevista). Para prompts reutilizáveis e de sistema, o template ganha; para prompts pontuais de tarefa, o gerador é mais rápido.

## Conexões
[System prompt de produção](system-prompt-de-producao.md) · [Elementos de um prompt](elementos-de-um-prompt.md) · [Gerador de prompts interativo](gerador-de-prompts-interativo.md) · [Engenharia de prompts](engenharia-de-prompts.md) · [Auto-crítica de LLM](auto-critica-de-llm.md) · testes como contrato · instruções de projeto (CLAUDE.md e AGENTS.md)

## Fontes
[Instrução-mestra de 12 seções (template)](../templates/instrucao-mestra-12-secoes.md)
