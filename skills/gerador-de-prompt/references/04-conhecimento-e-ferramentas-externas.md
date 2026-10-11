# 04 — Conhecimento e ferramentas externas

Carregue quando o problema é alucinação, conhecimento desatualizado, cálculo exato ou tarefa composta: RAG, PAL, ReAct, chaining.

## O insight central

Alucinação e erro de conta não se consertam com "não invente" nem com mais CoT — se consertam **tirando a responsabilidade do modelo**: conhecimento vem de fora (RAG), computação vai pro interpretador (PAL), interação vai pro ambiente (ReAct), complexidade se divide (chaining). O prompt vira orquestrador, não oráculo.

## As técnicas (escolha pela falha)

1. **RAG** (Lewis 2020; survey Gao 2023) — recupere passagens relevantes e condicione a geração nelas. Use quando o conhecimento é privado, atualizado ou citável. No prompt: `<contexto>` com as passagens + instrução "responda APENAS com base no contexto; se não estiver lá, diga que não está" + citação obrigatória por afirmação. Escada interna: naive (busca+cola) → advanced (re-ranking, query rewriting) → modular. A maioria dos "RAG ruim" é retrieval ruim, não prompt ruim.
2. **Generated knowledge** (Liu 2021) — sem infra de retrieval: peça primeiro "liste os fatos relevantes sobre X", depois responda usando os fatos. Versão pobre-e-digna do RAG pra conhecimento que o modelo TEM mas não ativa.
3. **PAL** (Gao 2022) — "escreva um programa Python que resolva; não calcule você mesmo". O LLM lê o problema, o interpretador computa. Use pra aritmética, datas, contagem, agregação. Determinismo onde importa.
4. **ReAct** (Yao 2022) — intercale `Thought → Action → Observation` com tools (busca, API). Reduz alucinação vs CoT puro porque o modelo verifica em vez de lembrar. É a semente do agente; se a conversa virar "que tools dar ao agente", a camada é harness — handoff.
5. **Prompt chaining** (Anthropic docs) — divida em subtarefas encadeadas: extrair citações → responder com base nelas; rascunhar → criticar → revisar. Cada elo com atenção total, transparente e depurável isoladamente. Use quando um prompt só faz duas coisas mal.

## Heurísticas / regras

- Fato inventado → RAG/citação. Conta errada → PAL. Precisa agir/verificar → ReAct. Duas tarefas num prompt → chaining.
- RAG: a cláusula "se não está no contexto, diga" vale mais que qualquer "seja preciso".
- Chaining: o contrato de saída de cada elo é a entrada do próximo — especifique-o duas vezes mais rígido (`02`).
- ART (Paranjape 2023) automatiza a escolha de raciocínio+tools via task library — cite como evolução, não como primeiro passo.

## Como entregar

1. Nomeie a falha e a delegação: "isso é erro de conta — o modelo não calcula, ele escreve o código que calcula".
2. Entregue o prompt orquestrador pronto (com `<contexto>`, o esqueleto do programa, ou os elos da chain numerados).
3. Feche com o teste da junta: "teste o elo 1 isolado antes de ligar o 2 — chain com elo podre falha silenciosamente".

## Conexões

- A resposta final ainda precisa de raciocínio → combine com `03`. Contrato entre elos → `02`. Virou agente/harness → fronteira da skill (handoff spec/context engineering).

<!-- fontes: gao-rag-survey, meta-ai-rag-blog, liu-generated-knowledge, gao-pal, paranjape-art, anthropic-prompt-chaining-docs (notas de curadoria), ingerido em 2026-07-05. Atualize via INGEST.md -->
