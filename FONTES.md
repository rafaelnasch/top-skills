# Materiais de apoio e fontes

As oito skills incluem **147 materiais em `sources/`**, além de oito índices de leitura. Esses materiais acompanham as pastas e os ZIPs individuais. As referências operacionais, scripts e templates que já existiam continuam incluídos; não entram nessa contagem.

| Biblioteca | Materiais | Conteúdo |
|---|---:|---|
| [criar-skill-ouro](skills/criar-skill-ouro/sources/README.md) | 12 | Estudo do padrão Agent Skills, ficha de procedência e dez notas de conceitos para composição de skills. |
| [gerador-de-prompt](skills/gerador-de-prompt/sources/README.md) | 71 | 35 conceitos, 33 fichas de fontes, dois templates genéricos e um mapa de leitura. |
| [book-to-skill](skills/book-to-skill/sources/README.md) | 8 | Oito documentos do projeto: apresentação, arquitetura, funcionamento, uso, instalação, perguntas frequentes, desempenho e estudo de carregamento progressivo. |
| [humanizer](skills/humanizer/sources/README.md) | 1 | Índice de procedência e links públicos; padrões e exemplos completos já estão no SKILL.md e no README do projeto. |
| [last30days](skills/last30days/sources/README.md) | 1 | Índice das fontes e módulos de pesquisa; o conteúdo temático é coletado a cada execução. |
| [notebooklm](skills/notebooklm/sources/README.md) | 6 | Seis documentos do notebooklm-py v0.3.3: apresentação, comandos, configuração, API Python, estabilidade e diagnóstico. |
| [elliott-jaques](skills/elliott-jaques/sources/README.md) | 18 | 17 notas: autor, pesquisa, mapa e 14 conceitos; mais uma bibliografia de fontes públicas. |
| [jesus-cristo](skills/jesus-cristo/sources/README.md) | 30 | Estudo das nove dimensões, mapa de leitura e 28 notas de conceitos bíblicos e cristológicos. |

## Como usar

- Comece pelo `SKILL.md`, que encaminha para a referência operacional necessária.
- Para aprofundar ou conferir a procedência, abra o índice `sources/README.md` da skill e escolha os arquivos pertinentes.
- Mantenha as pastas completas ao instalar. Links entre conceitos, fichas e referências apontam para arquivos que acompanham a distribuição.
- Material novo sem revisão fica em `sources/inbox/`, excluído do versionamento público, até passar pelo processo de ingestão da skill.

## Recorte da coleção

As fontes conceituais são edições públicas de notas, estudos, sínteses e fichas bibliográficas. A documentação dos projetos preserva a licença incluída. Datas e versões registram os materiais consultados; não significam atualização automática nem nova validação de todos os resultados históricos.

Foram excluídos identidade e contexto pessoal, registros de clientes e operações internas, links privados, cópias de contas, autenticação e credenciais. Livros, papers e cursos de terceiros permanecem como referências bibliográficas ou links públicos; seus textos integrais não acompanham esta coleção. Os estudos bíblicos mantêm as referências de passagens para consulta na tradução escolhida pelo leitor.

O [manifesto](manifest.json) lista todos os arquivos de fontes com SHA-256 e o hash de cada ZIP. Execute `python3.12 scripts/validate.py` para conferir o conteúdo local, os vínculos de fontes, os limites do frontmatter e a correspondência entre pastas e ZIPs.
