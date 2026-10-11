# 06 — Análise de prompt (modo ANALISAR)

Carregue no MODO ANALISAR: "analisa/melhora esse prompt", score, gaps, versão otimizada.

## O insight central

Análise sem diagnóstico vira embelezamento: troca palavras e mantém as falhas. O protocolo é **inferir o objetivo → pontuar por eixo → priorizar gaps → reescrever com diff explicado** — e nunca entregar a reescrita sem dizer o que estava quebrado e por quê.

## O protocolo

1. **Infira o objetivo real** e confirme em 1 frase ("esse prompt quer X pra público Y, certo?"). Se nem isso dá pra inferir, o diagnóstico já está pronto: objetivo ambíguo.
2. **Pontue 0–2 em cada eixo** (0 ausente · 1 fraco · 2 forte):
   - **Objetivo** — tarefa única e inequívoca?
   - **Contexto** — o que o modelo precisa saber está lá (e separado dos dados)?
   - **Contrato de saída** — estrutura, campos, critérios, cláusula de parada?
   - **Degrau** — a técnica bate com a natureza da tarefa (`01`)? (sobra técnica? falta?)
   - **Exemplos** — existem quando o formato é difícil? formato consistente? cobrem caso-limite?
   - **Guardrails** — casos-limite, recusas, anti-alucinação onde importa?
3. **Priorize os 2–3 gaps que mudam o resultado** (score baixo ≠ prioridade alta; contrato de saída ausente quase sempre vem primeiro).
4. **Reescreva** aplicando `02` (+ degrau de `03`/`04` se preciso) e entregue **antes → depois** com cada mudança justificada em 1 linha.
5. **Proponha o mini-eval**: 3–5 entradas de teste + o que observar em cada uma.

## Heurísticas / regras

- Sintoma → eixo: "ignora o formato" → contrato/exemplos; "alucina" → guardrails+RAG (`04`); "resposta rasa" → contexto ou degrau; "varia entre execuções" → temperatura ou self-consistency (`03`); "obedece metade" → curse of instructions: corte antes de adicionar.
- Respeite a voz do autor: conserte a engenharia, não o estilo — a menos que o estilo seja o problema.
- Prompt herdado de template alheio: desconfie de seções que não pagam custo neste uso — cortar é otimizar.
- Score total < 6/12 → não remende: reescreva do zero com `02` usando o original como matéria-prima.

## Como entregar

1. Abra com o veredito em 1 frase + score por eixo ("7/12 — forte em objetivo, zerado em contrato de saída").
2. Liste os 2–3 gaps priorizados com o porquê.
3. Entregue o antes → depois em bloco copiável, mudanças numeradas.
4. Feche com o mini-eval: "roda estes 3 casos; o caso 2 é o que quebrava o original".

## Conexões

- Reescrita usa `02` (anatomia) + `01` (degrau). Se o prompt é system prompt → critérios extras de `05`. Se o usuário quer comparar versões → `07`.

<!-- fontes: protocolo derivado do notas de curadoria (elementos-de-um-prompt, curse-of-instructions, template-mestre) + modo ANALISAR do prompt-craft, ingerido em 2026-07-05. Atualize via INGEST.md -->
