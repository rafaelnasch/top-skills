# INGEST — como a skill gerador-de-prompt cresce com o tempo

O índice [`sources/README.md`](sources/README.md) apresenta as fontes públicas já incluídas. Este playbook trata da revisão de material novo em `sources/inbox/`; essas entradas ficam separadas da biblioteca publicada.


Esta skill consome **referências curadas** (`references/*.md`), não material bruto.
Este arquivo é o playbook pra transformar fonte nova em inteligência — sem inchar contexto.

## Fontes de consulta e camadas de crescimento

1. **`sources/inbox/` (bruto)** — PDFs de papers, prompts coletados, system prompts extraídos, threads, exports. O usuário joga aqui livremente. **Nada aqui é lido em conversa normal.**
2. **`references/*.md` (curado)** — conciso, load-on-demand. É daqui que o roteador lê.
3. **Biblioteca pessoal opcional:** se o usuário mantiver um acervo externo, ele pode indicar uma fonte de lá. A skill funciona com as referências incluídas e não exige um wiki nem outro comando instalado.

A skill só melhora quando alguém **destila** (1)/(3) → (2). Esse alguém é o Claude, sob pedido.

## Gatilhos de ingestão

- usuário joga arquivo em `sources/inbox/` e diz "atualiza/ingere a skill";
- aponta nota do wiki e diz "puxa isso pra skill do gerador de prompt";
- no meio da conversa: "salva isso na skill de prompts" (ex.: uma técnica nova, um paper novo, um padrão que funcionou).

## Passo a passo

1. **Localize a fonte.** Em `sources/inbox/`, no wiki, ou na conversa. PDF grande: extraia texto e leia em pedaços com objetivo — não despeje inteiro no contexto.
2. **Extraia só o durável:** técnica nomeada + quando usar + número de evidência; heurísticas de decisão; frases canônicas com atribuição; padrões de prompts de produção. **Ignore** hype, listas de "10 prompts infalíveis" e repetição.
3. **Decida o destino.** Nova técnica de raciocínio → `03`. De conhecimento/tools → `04`. Padrão de system prompt → `05`. Método de eval → `07`. Mudança na escada/roteamento → `01`. Domínio realmente novo → crie `references/NN-<slug>.md` **e adicione a linha na tabela do `SKILL.md`** com o gatilho.
4. **Mantenha enxuto:** ~30–120 linhas por referência. Se passar de ~150, quebre com ponteiros.
5. **Registre procedência:** rodapé `<!-- fontes: arquivo / paper, ingerido em AAAA-MM-DD -->`.
6. **Não duplique:** `grep -r` na skill antes de criar; se o conceito existe, refine.

## Atenção especial deste domínio

- **Modelos mudam o degrau.** Quando um modelo novo tornar uma técnica redundante (como thinking fez com CoT explícito), atualize `01` e `03` — a escada é viva.
- **Número sem fonte não entra.** Todo ganho percentual citado precisa do paper/benchmark no rodapé.

## Princípio

A skill não melhora por acumular arquivos — melhora por **destilar** arquivos em regras
que o roteador aplica. Bruto entra em `sources/inbox/`; inteligência sai em `references/`.
