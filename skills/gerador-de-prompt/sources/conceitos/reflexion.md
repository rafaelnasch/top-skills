# Reflexion (reforço verbal)

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**Reflexion** é um framework de "reforço verbal": em vez de atualizar pesos com um sinal de reward (como no [RLHF — RL a partir de feedback humano](rlhf.md)), o agente **reflete em linguagem natural sobre as próprias falhas** e armazena essas reflexões em memória episódica, que entra no contexto das tentativas seguintes. Proposto por Shinn et al. (2023) em "Reflexion: Language Agents with Verbal Reinforcement Learning" — aprendizado por tentativa-erro sem nenhum fine-tuning, tudo via contexto ([Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md) como mecanismo de "gradiente").

A arquitetura tem três módulos: o **Actor** gera ações/saídas (tipicamente com [Chain-of-Thought (CoT)](chain-of-thought.md) ou [ReAct prompting (Reason + Act)](react-prompting.md) por baixo); o **Evaluator** pontua a trajetória (testes unitários em código, heurísticas ou o próprio LLM como juiz); e o **Self-Reflection** converte o sinal de avaliação em **feedback linguístico específico** ("falhei porque assumi X; na próxima, verificar Y"), gravado na memória episódica. O loop tentativa → avaliação → reflexão → nova tentativa roda até passar ou estourar o limite — um ciclo de execução de agentes com memória entre episódios.

O número-vitrine: **91% pass@1 no HumanEval** (geração de código), contra **80% do GPT-4 base** — na época, estado da arte. Também ganhos fortes em tomada de decisão sequencial (ALFWorld, +22 pontos absolutos) e raciocínio com busca (HotPotQA, +20). A chave em código é o Evaluator objetivo: testes que passam ou falham dão sinal externo confiável para a reflexão morder.

É a materialização mais completa da [Auto-crítica de LLM](auto-critica-de-llm.md) — e herda sua ressalva (Eric Jang, 2023): autocrítica sem sinal externo pode girar em falso; Reflexion funciona melhor onde há avaliador verificável. Diferenças de família: [Self-consistency](self-consistency.md) agrega tentativas *paralelas* por voto; Reflexion itera tentativas *sequenciais* com aprendizado verbal; [Tree of Thoughts (ToT)](tree-of-thoughts.md) busca *dentro* de uma tentativa. Em agentes de código modernos, o padrão Reflexion vive no harness (estrutura de execução de agentes, separação entre modelo e estrutura de execução): rode os testes, devolva o erro ao modelo, repita.

## Conexões
[Auto-crítica de LLM](auto-critica-de-llm.md) · [ReAct prompting (Reason + Act)](react-prompting.md) · [Chain-of-Thought (CoT)](chain-of-thought.md) · [Self-consistency](self-consistency.md) · [Tree of Thoughts (ToT)](tree-of-thoughts.md) · ciclo de execução de agentes · estrutura de execução de agentes · [RLHF — RL a partir de feedback humano](rlhf.md) · [Aprendizado em contexto (in-context learning)](aprendizado-em-contexto.md)

## Fontes
[Reflexion: Language Agents with Verbal Reinforcement Learning](../fontes/shinn-reflexion.md)
