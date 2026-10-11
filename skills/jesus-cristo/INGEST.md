# INGEST — como a skill Jesus Cristo cresce com o tempo

Esta skill consome **referências curadas** (`references/*.md`), não material bruto. Este arquivo é o playbook pra transformar fonte nova em inteligência da skill — sem inchar o contexto e **sem jamais corromper a fidelidade à Escritura.**

## A regra de ouro: duas camadas

1. **`sources/` (inbox de material bruto)** — estudos, PDFs de comentários, sermões, transcrições, exports do Wiki (biblioteca pessoal opcional). O usuário joga aqui livremente. **Nada aqui é lido numa conversa normal.** É arquivo morto até ser destilado.
2. **`references/*.md` (o que a skill usa)** — curado, conciso, load-on-demand, com referência bíblica preservada. É daqui que o roteador lê.

As referências curadas das nove dimensões estão em `references/`. Uma biblioteca pessoal é opcional; a skill não presume acesso a estudos ou índices externos.

## Gatilhos de ingestão

Rode este playbook quando o usuário:
- jogar arquivo(s) em `sources/` e disser "atualiza a skill" / "ingere isso";
- apontar um arquivo no Wiki (biblioteca pessoal opcional) e disser "puxa isso pra skill";
- no meio de uma conversa disser "salva isso na skill de Jesus" / "isso entra na skill".

## Passo a passo

1. **Localize a fonte.** Em `sources/`, na biblioteca pessoal opcional, ou na própria conversa. Se for PDF/ePub grande, extraia texto (`pandoc arquivo.epub -t plain -o /tmp/x.txt`) e leia em pedaços com objetivo — não despeje o arquivo inteiro no contexto.
2. **Extraia só o durável.** Procure: frameworks/estruturas nomeadas (as 9 dimensões, os 7 sinais, os "Eu Sou"), protocolos (leitura orante), chaves de parábola, faces da expiação, profecias/tipos com o elo no NT, frases canônicas com referência exata. **Ignore** enchimento e repetição.
3. **Preserve a referência bíblica.** Toda afirmação teológica carrega livro cap:versículo. Sem isso, não entra.
4. **Decida o destino.** Bate com uma referência existente (`01`–`11`)? → **atualize** (adicione uma seção, não reescreva o que já está bom). É um domínio novo (ex.: "orações e Salmos", "festas judaicas em Cristo", "ética específica")? → **crie** `references/12-<slug>.md` e **adicione a linha na tabela do `SKILL.md`** com o gatilho de "quando carregar".
5. **Mantenha enxuto.** Cada arquivo ~40–120 linhas. Se passar de ~150, quebre em sub-tópicos com ponteiros.
6. **Registre a procedência.** No fim da referência, a linha `<!-- fontes: ... ingerido em AAAA-MM-DD -->`.
7. **Não duplique.** `grep` nas referências antes de criar; se o conceito já existe, refine.

## Guardas de fidelidade (invioláveis — específicas desta skill)

- **Nunca destile em algo que invente Escritura** ou ponha palavra nova na boca de Jesus. Citação = texto real com referência; o resto é aplicação, marcada como tal.
- **Preserve o mistério onde a fonte o preserva** (Trindade, união hipostática) — não "resolva" o que a Escritura deixa aberto.
- **Distinga tradição de texto.** Se a fonte trouxer interpretação de uma corrente específica, registre como interpretação, não como "a Bíblia diz".
- **Ao ingerir de tradições diferentes,** não force uma leitura única sobre pontos legitimamente debatidos — nomeie que há leituras distintas.

## Biblioteca pessoal opcional

Se uma fonte estiver em uma biblioteca pessoal, o usuário pode indicar seu caminho. Leia-a somente quando houver pedido de ingestão. As referências resultantes devem continuar independentes daquela biblioteca; não crie links para arquivos privados na distribuição pública.

## Princípio

A skill não melhora por acumular arquivos — melhora por **destilar** arquivos em protocolos e chaves que o roteador aplica, sempre com a referência bíblica intacta. Bruto entra em `sources/`; inteligência (fiel) sai em `references/`.
