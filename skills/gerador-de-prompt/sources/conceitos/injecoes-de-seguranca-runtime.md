# Injeções de segurança em runtime

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Injeções de segurança em runtime** são instruções extras que o produto (não o usuário) insere dinamicamente na conversa quando detectores/classificadores flagram uma violação potencial — defesa em profundidade via prompts, injetada **depois** da mensagem do usuário.

A coleção histórica descrita na ficha de fonte inclui exemplos de instruções condicionais relacionadas a direitos autorais e a conteúdo potencialmente nocivo, acrescentadas ao contexto conforme a situação detectada. Esses exemplos são tratados como material de estudo, sem confirmação da arquitetura atual de um produto.

A lição de arquitetura: o [System prompt de produção](system-prompt-de-producao.md) **não é a única camada**. O padrão de produção é *classificador → injeção contextual dinâmica* — prompts também são mecanismo de **RUNTIME**, não só de design-time. A injeção chega depois da mensagem do usuário de propósito: o [O fim do prompt tem mais peso](fim-do-prompt-tem-mais-peso.md), então a instrução defensiva injetada por último ganha a disputa de atenção contra o jailbreak que veio antes.

Há uma ironia técnica proposital: é a mesma mecânica do *prompt injection* ofensivo — texto inserido no contexto pra redirecionar o modelo — só que usada **defensivamente**, pelo dono do sistema, com gatilho de classificador. Pra quem pratica [Engenharia de prompts](engenharia-de-prompts.md) em produtos, o takeaway é desenhar o sistema em camadas: prompt estático + detectores + injeções condicionais, em vez de tentar prever todo caso-limite no prompt de design-time.


## Conexões
[System prompt de produção](system-prompt-de-producao.md) · [O fim do prompt tem mais peso](fim-do-prompt-tem-mais-peso.md) · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[System prompts de produção do Claude (coleção extraída)](../fontes/claude-system-prompts-producao.md)
