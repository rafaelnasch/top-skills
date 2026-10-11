# 08 — Checklist de decisão (pré-voo do prompt)

Carregue quando "vou escrever um prompt pra X — por onde começo?": pré-voo completo, passo a passo.

## O insight central

Antes de escrever qualquer linha, três decisões definem 90% do resultado: **modo** (criar/analisar/sistema), **degrau** (a técnica mínima que a tarefa pede) e **contrato** (como a saída será verificada). O checklist percorre as três e te larga com o prompt testável — o antídoto contra o vício de colecionar técnica ("vou usar ToT porque é impressionante") e contra o prompt-esperança (escreve, torce, cola de novo).

## O checklist

0. **Modo?** Prompt novo → siga. Prompt existente falhando → vá direto pra `06`. Instrução-mestra/system → `05` (e volte aqui pro degrau).
1. **Objetivo em 1 frase** — tarefa única, público, tamanho. Não consegue? Pare: o problema é o objetivo, não o prompt.
2. **Modelo-alvo?** Thinking nativo → esqueça CoT explícito; modelo pequeno → esqueça CoT também (emergência de escala); API parseável → contrato JSON.
3. **Natureza da tarefa → degrau** (`01`): raciocínio (`03`) · conhecimento/fato (`04`-RAG) · conta exata (`04`-PAL) · ambiente/tools (`04`-ReAct) · composta (`04`-chaining) · formato/estilo difícil (few-shot em `02`) · nada disso → zero-shot bem escrito e pronto.
4. **Monte com a anatomia** (`02`): instrução separada dos dados (tags XML), papel com escopo se agregar, exemplos SE o formato pedir (consistentes + 1 caso-limite).
5. **Contrato de saída** — estrutura, campos obrigatórios, critérios de aceitação, cláusula de parada ("se faltar info crítica, liste e pare"). *Gate: dá pra verificar a resposta objetivamente? Se não, o contrato está fraco.*
6. **Passe anti-negativas + posição** — proibições viram direções; contrato fácil de localizar, com posição testada no modelo-alvo; corte toda regra que não paga custo (curse of instructions).
7. **Teste em 3 casos reais** (1 típico, 1 limite, 1 fora do escopo — este último testa a recusa). Falhou? A falha aponta o eixo (`06`) — conserte UM eixo e reteste.
8. **Vai rodar em volume?** → suite de eval + regressão (`07`). Uso pontual → pare no 7, está pronto.

## Heurísticas / regras

- 80% dos prompts morrem bem no passo 4–5: zero-shot + contrato rígido. Desconfie de quem começa pelo degrau 4.
- O caso "fora do escopo" do passo 7 é o mais negligenciado — todo prompt de produção recebe entrada que não devia.
- Se você voltou ao passo 7 três vezes no mesmo eixo, o problema é de camada: ou falta RAG/PAL (delegação), ou é harness/spec — não insista em prosa.

## Como entregar

1. Percorra o checklist NOMEANDO cada decisão ("modo criar, modelo thinking, tarefa de extração → zero-shot + contrato JSON, sem CoT").
2. Entregue o prompt do passo 4–6 pronto em bloco copiável.
3. Feche com os 3 casos do passo 7 já sugeridos: "roda estes; me traga o pior".

## Conexões

- Cada passo aponta sua referência: degrau → `01` · anatomia/contrato → `02` · raciocínio → `03` · delegação → `04` · sistema → `05` · falhou → `06` · volume → `07`.

<!-- fontes: destilação do notas de curadoria (MOC engenharia-de-prompts), ingerido em 2026-07-05. Atualize via INGEST.md -->
