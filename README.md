# top-skills

Oito skills selecionadas por Rafael Nasch para compartilhar com o Dr. Sharbo. Cada pasta contém o `SKILL.md` e os arquivos de apoio necessários. As cópias públicas foram adaptadas para uso fora do ambiente original.

| Skill | Para que serve | Exemplo de uso |
|---|---|---|
| [Criar Skill Ouro](skills/criar-skill-ouro/SKILL.md) | Cria skills de especialistas ou métodos com roteamento por intenção e referências sob demanda. | `/criar-skill-ouro Crie uma skill sobre meu método de atendimento.` |
| [Gerador de Prompt](skills/gerador-de-prompt/SKILL.md) | Cria, analisa e melhora prompts e instruções para agentes. | `/gerador-de-prompt Melhore este prompt e defina o formato da resposta.` |
| [Book to Skill](skills/book-to-skill/SKILL.md) | Transforma livros e documentos em conhecimento reutilizável por agentes. | `/book-to-skill Transforme este documento em uma skill.` |
| [Humanizer](skills/humanizer/SKILL.md) | Revisa textos com marcas de escrita artificial, preservando o conteúdo e a voz do autor. | `/humanizer Revise este texto mantendo o meu jeito de escrever.` |
| [Last 30 Days](skills/last30days/SKILL.md) | Pesquisa conversas e informações recentes em diversas fontes. | `/last30days O que se discutiu sobre inteligência artificial na educação?` |
| [NotebookLM](skills/notebooklm/SKILL.md) | Opera o NotebookLM para organizar fontes, consultar conteúdo e gerar materiais. | `/notebooklm Crie um notebook com estes documentos.` |
| [Elliott Jaques](skills/elliott-jaques/SKILL.md) | Analisa níveis de trabalho, estrutura organizacional, capacidade e remuneração. | `/elliott-jaques Ajude a avaliar as camadas de gestão desta organização.` |
| [Jesus Cristo](skills/jesus-cristo/SKILL.md) | Apoia estudo bíblico, leitura orante e reflexão cristocêntrica. | `/jesus-cristo Estude comigo o Sermão do Monte.` |

## Baixar uma skill

Abra [downloads/](downloads/) e escolha o ZIP da skill desejada. Para baixar todas as pastas, use **Code → Download ZIP** no GitHub.

## Instalar no Claude.ai

- [ ] Baixe o ZIP individual em `downloads/`.
- [ ] No Claude, habilite a execução de código em **Settings → Capabilities**, se necessário.
- [ ] Abra **Customize → Skills**, clique em **+ → Create skill → Upload a skill**.
- [ ] Envie o ZIP de uma skill por vez e habilite-a.
- [ ] Abra uma conversa e faça um pedido relacionado à skill.

O caminho de instalação segue o [guia oficial do Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude). Skills que executam programas dependem das ferramentas e permissões disponíveis no aplicativo. NotebookLM exige instalação e autenticação próprias; o arquivo da skill, por si só, não conecta sua conta Google.

## Instalar no Codex ou Claude Code

- [ ] Baixe e descompacte o repositório.
- [ ] No **Codex**, copie a pasta da skill para `~/.agents/skills/<nome-da-skill>/`.
- [ ] No **Claude Code**, copie a pasta da skill para `~/.claude/skills/<nome-da-skill>/`.
- [ ] Preserve a pasta inteira, incluindo `references/`, `scripts/`, `assets/` e outros arquivos que existirem.
- [ ] Se uma skill com o mesmo nome já estiver instalada, escolha como atualizar antes de copiar.
- [ ] Abra uma nova sessão e confirme que a skill aparece.

Você também pode pedir ao agente: "Instale as skills deste repositório para uso pessoal no meu agente, preservando instalações existentes: https://github.com/rafaelnasch/top-skills".

## Requisitos adicionais

| Skill | Requisito |
|---|---|
| Book to Skill | Python 3.9+; bibliotecas de extração variam conforme PDF, EPUB, DOCX e outros formatos. O `SKILL.md` orienta a instalação. |
| Last 30 Days | Python 3.12+; Node.js para integrações opcionais. Algumas fontes exigem chaves próprias. |
| NotebookLM | `notebooklm-py`, ambiente compatível e autenticação na própria conta Google, conforme o `SKILL.md`. |
| Demais skills | Um agente que suporte skills e leitura dos arquivos de referência. |

## Conteúdo e créditos

As skills de terceiros mantêm seus créditos e licenças. Consulte [CREDITOS.md](CREDITOS.md). Este repositório distribui cópias selecionadas, não promete atualização automática nem inclui livros, credenciais, sessões autenticadas ou dados de clientes.

Validação do pacote, com Python 3.12 ou superior: `python3.12 scripts/validate.py`.
