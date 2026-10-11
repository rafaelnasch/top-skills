# 03 — Técnicas de raciocínio

Carregue quando a tarefa é raciocínio multi-step: CoT, zero-shot CoT, self-consistency, ToT, reflexion.

## O insight central

Gerar os passos dá ao modelo espaço de computação serial em tokens — o transformer acerta um subpasso de cada vez o que erraria de uma vez. Mas é **habilidade emergente de escala** (Wei 2022, ~100B+): em modelo pequeno a cadeia sai fluente e ilógica. E em 2026: **modelos com raciocínio nativo (thinking) já fazem CoT internamente** — instruir "think step by step" neles é redundante; o valor migrou pra self-consistency, ToT e auto-crítica, que operam SOBRE as cadeias.

## As técnicas (em ordem de custo)

1. **Zero-shot CoT** (Kojima 2022) — anexe "Let's think step by step" (ou peça os passos antes da resposta). MultiArith 17.7%→78.7% no InstructGPT. Custo quase zero; primeiro degrau de raciocínio.
2. **Few-shot CoT** (Wei 2022) — 2–8 exemplares `pergunta → raciocínio → resposta`. Use quando o TIPO de raciocínio importa (você mostra o caminho certo). PaLM 540B + 8 exemplares bateu o SOTA fine-tuned no GSM8K.
3. **Self-consistency** (Wang 2022) — amostre N cadeias (temperatura >0, N=5–10) e vote na resposta majoritária. +17.9% sobre CoT no GSM8K. Use quando execuções divergem; só vale se a resposta final é comparável (número, classe, opção).
4. **ToT** (Yao 2023) — decomponha em "thoughts", gere k candidatos por passo, avalie (o próprio modelo julga "certo/talvez/impossível"), busque com backtracking. Game of 24: 4% (CoT) → 74%. Caro; só pra exploração real com becos sem saída. Versão-prompt barata (Hulbert): "imagine três especialistas respondendo passo a passo; quem errar, sai".
5. **Reflexion / auto-crítica** (Shinn 2023; Jang 2023) — gerar → criticar → regenerar com a crítica na memória. HumanEval 91% vs 80% do GPT-4 base. Funciona porque **criticar é mais fácil que gerar** — mas precisa de sinal externo (teste, erro, regra violada); auto-crítica sem critério converge pra cosmética.

## Heurísticas / regras

- Cadeia legível ≠ raciocínio fiel: use os passos pra depurar, não como prova.
- Divergência entre execuções é o gatilho do self-consistency, não "quero mais qualidade".
- Se a falha é de FATO (não de lógica) → o problema é conhecimento: vá pra `04` (RAG).
- Se a falha é de CONTA → PAL (`04`), não mais CoT: código não erra aritmética.
- Modelo thinking: pule 1–2; considere 3–5 se ainda diverge.

## Como entregar

1. Nomeie o degrau e por quê ("diverge entre execuções → self-consistency com N=5, votação na resposta final").
2. Entregue o prompt com a técnica já embutida (exemplares CoT prontos, não "adicione exemplos").
3. Feche com o teste e o próximo degrau se falhar: "se com N=5 ainda divergir, o problema não é amostragem — me mostra os casos que subimos pra ToT".

## Conexões

- Falha de fato/conta/ambiente → `04`. Prompt de raciocínio de alto volume → validar ganho em `07`. Contrato de saída da resposta final → `02`.

<!-- fontes: wei-chain-of-thought, kojima-zero-shot-reasoners, wang-self-consistency, yao-tree-of-thoughts, shinn-reflexion, eric-jang-llm-self-critique (notas de curadoria), ingerido em 2026-07-05. Atualize via INGEST.md -->
