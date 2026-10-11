# 01 — Diagnóstico de entrada + a escada de técnicas

Carregue no diagnóstico de entrada: que degrau essa tarefa pede? (roteador-mestre da skill)

## O insight central

Quem chega pedindo prompt quase nunca nomeia a causa real. O diagnóstico tem três perguntas, **nesta ordem**:

1. **MODO** — o que o usuário quer de você?
   - **CRIAR**: prompt novo pra uma tarefa → `02-anatomia-do-prompt.md` (+ a técnica do degrau).
   - **ANALISAR**: prompt existente que falha → `06-analise-de-prompt.md`.
   - **SISTEMA**: system prompt / instrução-mestra / GPT custom → `05-system-prompts-de-producao.md`.
2. **NATUREZA da tarefa** — o que o modelo precisa fazer? (tabela abaixo)
3. **O QUE JÁ FALHOU** — se nada foi tentado, comece no degrau mais baixo plausível. Se algo falhou, a falha diz o degrau: resposta errada em conta = computação (PAL); fato inventado = conhecimento (RAG); raciocínio torto = CoT/self-consistency; formato errado = contrato de saída, não técnica nova.

## A escada (suba só com falha demonstrada)

```
0. zero-shot bem escrito        ← 80% dos casos morrem aqui
1. + contrato de saída rígido   ← formato errado se conserta aqui, não com técnica
2. few-shot (2-5 exemplos)      ← quando o formato/estilo é difícil de descrever
3. CoT / zero-shot CoT          ← raciocínio multi-step (modelo sem thinking nativo)
4. self-consistency / ToT       ← respostas divergem entre execuções / precisa explorar
5. RAG / PAL / ReAct / chaining ← o problema é conhecimento, computação ou ambiente
6. otimização automática + eval ← prompt de alto volume onde 2% importa
```

**Regra de ouro:** cada degrau custa tokens, latência e manutenção. O degrau mínimo que resolve é o certo.

## Tabela tarefa → técnica

| A tarefa exige... | Degrau/técnica | Referência |
|---|---|---|
| Instrução simples, formato claro | zero-shot + contrato de saída | `02` |
| Estilo/formato difícil de descrever | few-shot (formato consistente) | `02` |
| Classificação/extração com casos-limite | few-shot com exemplos dos limites | `02` |
| Raciocínio multi-step (lógica, matemática, planejamento) | CoT; se diverge, self-consistency | `03` |
| Exploração com becos sem saída (puzzle, planejamento profundo) | ToT | `03` |
| Auto-correção iterativa com feedback | reflexion / auto-crítica | `03` |
| Conhecimento fora do modelo / atualizado / citável | RAG (ou generated knowledge se leve) | `04` |
| Aritmética exata, datas, contagem | PAL — código, não prosa | `04` |
| Interagir com ambiente/tools/busca | ReAct | `04` |
| Tarefa composta (extrair→transformar→formatar) | prompt chaining | `04` |
| Prompt estável de alto volume | otimização + eval | `07` |

## Heurísticas / regras

- **Modelo com raciocínio nativo (thinking)**: pule o degrau 3 — CoT explícito é redundante e às vezes piora; vá direto de contrato de saída pra técnica de conhecimento/ferramenta.
- **Falha de formato NUNCA se resolve com técnica de raciocínio** — se resolve com contrato de saída e exemplos.
- **Alucinação não se resolve com "não invente"** — se resolve com RAG, citação obrigatória e cláusula de parada.
- Se o pedido é sobre o **agente inteiro** (tools, memória, multi-turno), a camada é outra: handoff pra spec/context engineering.

## Como entregar

1. Abra nomeando modo + degrau: "isso é modo CRIAR, tarefa de raciocínio — degrau 3, CoT; não precisa de RAG porque o conhecimento está no input".
2. Justifique o degrau com 1 razão (e 1 número de paper quando houver).
3. Carregue a referência do degrau e entregue o prompt pronto.
4. Feche com o teste: "roda nesses 3 casos; se divergir entre execuções, subimos pra self-consistency".

## Conexões

- Modo CRIAR → `02-anatomia-do-prompt.md` · Raciocínio → `03` · Conhecimento/tools → `04` · SISTEMA → `05` · ANALISAR → `06` · Otimizar → `07` · Pré-voo completo → `08`.

<!-- fontes: cluster biblioteca de curadoria original (MOC engenharia-de-prompts), ingerido em 2026-07-05. Atualize via INGEST.md -->
