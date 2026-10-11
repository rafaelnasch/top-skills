# 07 — Otimização e eval

Carregue quando o prompt já é bom mas precisa de mais, o usuário quer A/B, ou pergunta "como sei se melhorou?".

## O insight central

O prompt artesanal tem teto — e a evidência é constrangedora: **APE** (Zhou 2022) pôs um LLM pra gerar e testar instruções e achou uma melhor que a humana ("Let's work this out in a step by step way to be sure we have the right answer"); **OPRO** (Yang 2023) otimizou por meta-prompt com histórico (instrução, score) e achou "Take a deep breath and work on this problem step-by-step" (80,2% contra 71,8% no GSM8K, diferença de 8,4 pontos percentuais com PaLM 2-L como avaliador, Tabela 1 do paper). Ninguém teria chutado essas frases. Moral: **acima de certo volume, quem otimiza prompt é avaliação sistemática, não intuição** — a sua incluída.

## O protocolo do mini-eval (o mínimo digno)

1. **Colete 5–15 casos reais** (entrada + saída esperada ou critério de aceite). Inclua 2–3 casos-limite — é onde prompts quebram.
2. **Defina o critério por caso:** exato (número/classe: comparação direta) ou rubrica (1–5 em fidelidade/formato/completude — LLM-as-judge com rubrica explícita serve, com calibração humana em amostra).
3. **Baseline:** rode o prompt atual em todos os casos. Anote score e falhas.
4. **Uma variação por vez** (instrução OU exemplos OU contrato — nunca tudo junto; senão você não sabe o que pagou).
5. **Compare no mesmo conjunto**, mesma temperatura. Diferença pequena em N pequeno é ruído — aceite só ganhos claros ou em casos-limite.
6. **Congele e registre:** versão vencedora + data + score, e a suite vira **teste de regressão** — roda após toda edição futura (system prompts quebram em silêncio; `05`).

## Escalando (quando o mini-eval não basta)

- **Geração de candidatos via LLM** (espírito do APE): "gere 8 variações desta instrução mantendo o contrato" → rode a suite em todas → mantenha a campeã. Barato e surpreendentemente eficaz.
- **Meta-prompt com histórico** (espírito do OPRO): inclua as (variação, score) anteriores no prompt do gerador e peça a próxima — o LLM extrapola a trajetória.
- **Soft prompts / prompt tuning** (Lester 2021, Li & Liang 2021): fronteira dura — exige acesso aos pesos/embeddings; fora do alcance via API de chat. Cite pra calibrar expectativa, não como próximo passo.

## Heurísticas / regras

- Sem baseline não existe "melhorou". Primeiro mede, depois mexe.
- Otimize o prompt que roda mil vezes, não o que roda uma.
- Ganho de eval em benchmark ≠ ganho no SEU caso: a suite tem que ser dos seus casos reais.
- Se a suite passa e o uso real falha → a suite está pobre em casos-limite; conserte a suite antes do prompt.

## Como entregar

1. Monte a suite COM o usuário (peça os casos reais; não invente todos).
2. Entregue baseline + variações + tabela de scores, e a recomendação com 1 razão.
3. Feche com a regressão: "guarda essa suite; ela roda de novo em toda edição do prompt".

## Conexões

- As variações se constroem com `02`–`04`. Regressão de system prompt → `05`. Diagnóstico do que variar → `06`.

<!-- fontes: zhou-ape, yang-opro, sun-prompt-oirl, lester-prompt-tuning, li-liang-prefix-tuning, otimizacao-automatica-de-prompts (notas de curadoria), ingerido em 2026-07-05. Atualize via INGEST.md -->
