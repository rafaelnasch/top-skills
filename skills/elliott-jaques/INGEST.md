# INGEST — como a skill do Elliott Jaques cresce com o tempo

Esta skill consome **referências curadas** (`references/*.md`), não material bruto.
Este arquivo é o playbook pra transformar fonte nova em inteligência — sem inchar contexto.

## Duas camadas

1. **`sources/` (bruto)** — ePubs, PDFs, transcrições, exports, notas do wiki.
   O usuário joga aqui livremente. **Nada aqui é lido em conversa normal.**
2. **`references/*.md` (curado)** — conciso, load-on-demand. É daqui que o roteador lê.

A skill só melhora quando alguém **destila** (1) → (2). Esse alguém é o Claude, sob pedido.

## Gatilhos de ingestão

- usuário joga arquivo em `sources/` e diz "atualiza/ingere a skill";
- aponta nota de sua biblioteca pessoal e diz "puxa isso pra skill";
- no meio da conversa: "salva isso na skill do Jaques".

## Fontes de alto valor pra buscar no futuro

- **Requisite Organization** (1989/1996) e **Human Capability** (1994) — os textos
  integrais refinariam `02`–`06` com os protocolos originais (hoje derivados de
  fontes secundárias verificadas).
- ROII working papers (requisite.org) — especialmente os de medição.
- GO Society (globalro.org) — casos de implementação e vídeos de praticantes.
- *Systems Leadership* (Macdonald/Burke/Stewart) — a extensão prática australiana.
- A banda 90–120% do felt-fair pay contra o texto de 1961 (hoje é leitura secundária).

## Passo a passo

1. **Localize a fonte.** Em `sources/`, no wiki, ou na conversa. ePub/PDF grande:
   extraia texto (`pandoc x.epub -t plain -o /tmp/x.txt`) e leia em pedaços com
   objetivo — não despeje inteiro no contexto.
2. **Extraia só o durável:** frameworks nomeados, protocolos passo-a-passo, regras
   de decisão, frases canônicas verificáveis, casos com números.
3. **Decida o destino.** Bate com referência existente → **atualize**. Domínio
   novo → crie `references/NN-<slug>.md` e **adicione a linha na tabela do
   `SKILL.md`** com o gatilho.
4. **Mantenha enxuto:** ~30–120 linhas por referência; passou de ~150, quebre.
5. **Registre procedência:** rodapé `<!-- fontes: ..., ingerido em AAAA-MM-DD -->`.
6. **Não duplique:** `grep` antes de criar; se o conceito existe, refine.
7. **Citações novas de Jaques:** só entram em `11-canonical-phrases.md` com fonte
   primária — a obra dele é cheia de atribuições erradas (a começar pela grafia).

## Princípio

A skill não melhora por acumular arquivos — melhora por **destilar** arquivos em
regras que o roteador aplica. Bruto entra em `sources/`; inteligência sai em `references/`.
