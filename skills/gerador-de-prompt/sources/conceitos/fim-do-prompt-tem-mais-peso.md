# O fim do prompt tem mais peso

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

A posição de instruções e dados pode influenciar a resposta de um modelo. Esta nota registra uma **heurística de composição de prompts** atribuída a Leonardo Leitão na trilha AI-Driven Development: deixar o contrato de saída e outras instruções decisivas próximos do ponto em que a resposta será produzida. A heurística não estabelece uma lei universal de atenção nem garante que todo modelo dê mais peso ao final.

Aplicações metodológicas:
- Separar os dados volumosos das instruções e tornar o formato de saída fácil de localizar.
- Conferir se mensagens recentes com erros, exemplos inadequados ou premissas falsas estão desviando a tarefa.
- Comparar posições alternativas das instruções com casos de teste do uso real, em vez de presumir ganho.

A posição complementa o problema da [Curse of Instructions](curse-of-instructions.md): quantidade, conflito entre regras e organização do contexto também afetam a aderência.

## Conexões
[Elementos de um prompt](elementos-de-um-prompt.md) · [Curse of Instructions](curse-of-instructions.md) · [Prompt chaining (encadeamento de prompts)](prompt-chaining.md)

## Fontes
[AI Driven Development — trilha da Formação.Dev (Leonardo Leitão)](../fontes/ai-driven-development-formacao-dev.md) (atribuição da heurística, curso introdutório, aulas 5–6).
