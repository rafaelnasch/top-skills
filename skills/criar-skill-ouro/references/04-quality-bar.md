# 04 — Barra de qualidade + self-audit

Rode em silêncio antes de declarar a skill pronta. Corrija inline o que falhar.

## Checklist da description (o gatilho)

- [ ] Diz **o que faz** E **quando usar** (contextos específicos, não só o tema).
- [ ] É **pushy** — combate o sub-disparo. Inclui "Use SEMPRE que..." com situações concretas.
- [ ] Inclui casos em que o usuário **não nomeia** o especialista mas precisa da skill ("tô sem tempo" → skill do Ferriss).
- [ ] Inclui pedidos cirúrgicos reais ("roda um fear-setting", "faz o 80/20 disso").
- [ ] Diferencia de skills vizinhas/competidoras quando houver risco de confusão.
- [ ] Até 450 caracteres. Específica, com o que faz e quando usar.

**Ruim:** "Ajuda com produtividade."
**Bom:** "Use SEMPRE que o usuário estiver sobrecarregado, dizendo 'sem tempo', querendo eliminar/automatizar/delegar... mesmo que não cite 'Tim Ferriss'."

## Checklist de estrutura

- [ ] `SKILL.md` < ~120 linhas; identidade na 1ª linha do corpo.
- [ ] Tabela de referência com **gatilho por linha** ("quando carregar").
- [ ] Cada referência: enxuta, com "Como entregar" e ponteiros.
- [ ] Existe `00-canon.md` (voz) e uma referência de roteador-mestre (diagnóstico de entrada).
- [ ] Existe um `decision-checklist` (entry-point "decide X").
- [ ] Camada de crescimento presente: `sources/README.md` + `INGEST.md`.
- [ ] Caminhos e nome da skill corretos em TODOS os arquivos (templates não deixaram `{{placeholder}}` solto).

## Checklist de alma (o mais importante)

- [ ] **Teste do transplante:** trocar o nome do especialista quebraria os comportamentos? Se não quebra, está genérico demais — re-derive (`03`).
- [ ] Os comportamentos refletem como ESTE especialista diagnostica/decide/ensina/fala.
- [ ] Há frases canônicas reais dele, não inventadas.
- [ ] Self-reference usa o ecossistema real dele.
- [ ] Fronteiras/recusas são específicas do domínio (não genéricas).

## Anti-padrões (não faça)

- Despejar todo o conhecimento no SKILL.md em vez de rotear pra referências.
- Referências que são resumo vago em vez de protocolo acionável.
- Description genérica que nunca dispara (ou que dispara pra tudo).
- Nascer sem a camada de crescimento (`sources/` + `INGEST.md`).
- Deixar `{{placeholders}}` dos templates sem preencher.
- Copiar comportamentos de outra persona sem derivar.

## Verificação mecânica final

```bash
find $HOME/.agents/skills/<nome> -type f | sort
wc -l $HOME/.agents/skills/<nome>/SKILL.md $HOME/.agents/skills/<nome>/references/*.md
grep -rn "{{" $HOME/.agents/skills/<nome>    # não deve sobrar placeholder

```
Abra uma nova sessão e confirme que a skill apareceu na lista de skills disponíveis. Valide também os limites de `name` e `description` por script antes de publicar ou gerar um ZIP.
