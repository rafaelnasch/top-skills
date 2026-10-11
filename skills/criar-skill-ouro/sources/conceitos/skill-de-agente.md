# Skill de agente: anatomia e natureza

No formato aberto **Agent Skills**, uma skill é uma pasta versionável que contém ao menos
`SKILL.md`: metadados para descoberta e instruções para executar um tipo de tarefa. Ela pode
incluir scripts, referências, assets e outros recursos. A skill não é um modelo nem uma
ferramenta nova; ela disponibiliza conhecimento e procedimento a um agente que já possui um
cliente, um ambiente e determinadas capacidades.

**Anatomia mínima**: pasta + `SKILL.md` com frontmatter (`name` em kebab-case minúsculo +
`description` contendo o gatilho — ver [description-como-gatilho](description-como-gatilho.md)). Pode ter dezenas de
arquivos, "mas a porta de entrada é exatamente esse arquivo". Nos ambientes mostrados no curso,
vive em `.claude/skills/` (claude-code) ou `.agents/skills/` (codex-openai) — dentro do
projeto, junto do código; compartilha entre ferramentas via link simbólico, entre projetos via
repositório Git + submodules. Caminhos adicionais e a necessidade de reiniciar ou recarregar
dependem do cliente; não são requisitos universais do padrão aberto.

## Núcleo do padrão aberto

A especificação oficial do **Agent Skills** padroniza o que existe **dentro da pasta**, não
onde ela deve ser instalada. `name` e `description` são obrigatórios; `license`,
`compatibility`, `metadata` e o experimental `allowed-tools` são opcionais. `scripts/`,
`references/` e `assets/` também são opcionais, e outros diretórios podem existir sem adquirir
semântica portátil por isso.

O mecanismo central é a divulgação progressiva:

1. o catálogo carrega somente `name` e `description` de cada skill disponibilizada ao modelo;
2. a ativação carrega o corpo inteiro de `SKILL.md`;
3. scripts, referências e assets entram apenas quando necessários.

Assim, a `description` não é só documentação: ela precisa tornar o job reconhecível antes que
o corpo esteja visível. O `SKILL.md` deve conter o núcleo comum e rotear detalhes condicionais
por caminho e gatilho claros. A documentação recomenda menos de 5.000 tokens e 500 linhas no
arquivo principal; são limites de desempenho, não critérios de validade.

`.agents/skills/` é uma convenção interoperável amplamente adotada, mas o formato não define
caminho de instalação, sintaxe de invocação, runtime, permissões, sandbox, distribuição ou
versionamento. A distinção completa entre norma, orientação de autoria e escolhas do cliente
está em [agent-skills-padrao-aberto-estudo](../estudos/agent-skills-padrao-aberto-estudo.md) e no mapa agent-skills-moc.



## Fonte pública

[Agent Skills: especificação](https://agentskills.io/specification). Nota de estudo derivada do padrão aberto, com aplicações locais removidas.
