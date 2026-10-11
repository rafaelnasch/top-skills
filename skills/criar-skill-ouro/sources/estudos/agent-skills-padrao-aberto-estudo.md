# Agent Skills: anatomia, ciclo e aplicação

> Nota de estudo do padrão aberto, baseada no levantamento datado de julho de 2026. Esta distribuição remove metadados e aplicações do acervo original; a documentação pública continua sendo a fonte normativa. Para esta coleção, adote `description` com até 450 caracteres mesmo quando uma especificação ou cliente admitir mais.

## Pergunta

**Como o Agent Skills transforma expertise em uma capacidade portátil para agentes, o que
o padrão realmente exige e como criar, avaliar e executar uma skill com utilidade,
compatibilidade e segurança?**

## Resposta executiva

Agent Skills é um formato aberto para empacotar **saber fazer**. A unidade mínima é uma
pasta com `SKILL.md`: frontmatter que permite descobrir a capacidade e corpo Markdown que
ensina o procedimento. Referências, scripts e assets podem acompanhar o arquivo.

Seu mecanismo central é a **divulgação progressiva**:

1. o cliente mostra ao modelo somente `name` e `description` das skills disponibilizadas;
2. quando uma parece relevante, carrega o `SKILL.md` completo;
3. só então abre ou executa recursos auxiliares quando a instrução pedir.

O padrão resolve a **portabilidade do pacote**, não todo o runtime. Ele não padroniza onde
instalar, como distribuir e versionar, qual sintaxe invoca, quais linguagens executam, como
permissões e sandbox funcionam nem se dois modelos obedecerão da mesma forma. “Escrever uma
vez” significa transportar a mesma pasta; não garante resultado idêntico em todo cliente.

**Síntese deste estudo:** uma skill só tem valor quando toda a cadeia funciona:

```text
descoberta
→ reconhecida pela description
→ ativada na tarefa certa
→ instrução útil carregada
→ recursos compatíveis acessados
→ execução segura
→ resultado melhor que o baseline
```

Cada elo pede um diagnóstico diferente. Validade estrutural, acionamento, qualidade de
saída e segurança não são a mesma coisa.

## Estado epistemológico

- **Normativo:** apenas o que a [especificação](https://agentskills.io/specification) define.
- **Orientação oficial:** guias de autoria, avaliação, scripts e implementação; são práticas
  recomendadas, não novos requisitos do formato.
- **Exemplo:** quickstart, `skills-ref` e repositório da Anthropic; demonstram possibilidades,
  mas não ampliam a norma.
- **Inferência deste estudo:** conclusões derivadas do conjunto são marcadas como tal.

## 1 · O modelo mental: catálogo, manual e oficina

| Camada | Analogia | Conteúdo | Quando entra no contexto |
|---|---|---|---|
| 1 · catálogo | etiqueta na lombada | `name` + `description` | início da sessão |
| 2 · manual | procedimento operacional | corpo inteiro de `SKILL.md` | ativação |
| 3 · oficina | gavetas e ferramentas | `references/`, `scripts/`, `assets/` | sob demanda |

A especificação estima cerca de 100 tokens por skill no catálogo; o guia de implementação
usa a faixa aproximada de 50–100. Ambos recomendam menos de 5.000 tokens para as instruções
ativadas. O custo dos recursos depende do que for aberto ou executado. Assim, dezenas de
capacidades podem ficar disponíveis sem que dezenas de manuais ocupem a janela desde o começo.

Consequências:

- A `description` é índice e roteador. O que está apenas no corpo não ajuda a descoberta.
- O corpo deve conter o núcleo usado em toda execução, não uma enciclopédia.
- Uma referência só é útil se o corpo disser **quando** carregá-la.
- Um script compra determinismo onde raciocínio repetido ou operação frágil não deveria ser
  reimprovisado.
- Um asset fornece material estático — template, schema, imagem ou tabela — sem precisar
  reconstruí-lo a cada uso.

Isso materializa skill-como-peso-estatistico-no-contexto e aproxima uma skill de uma
biblioteca carregada dinamicamente: uma entrada leve resolve o endereço; o conteúdo pesado
só entra quando há demanda.

## 2 · O contrato normativo de `SKILL.md`

### Estrutura

```text
minha-skill/
├── SKILL.md          # obrigatório
├── scripts/          # opcional
├── references/       # opcional
├── assets/           # opcional
└── outros-arquivos/  # permitidos, mas não padronizados
```

`SKILL.md` começa com frontmatter YAML delimitado por `---` e continua com Markdown.

### Frontmatter

| Campo | Obrigatório? | Contrato |
|---|---|---|
| `name` | sim | 1–64 caracteres; alfanuméricos minúsculos e hífens; sem hífen nas pontas ou `--`; igual ao diretório pai |
| `description` | sim | 1–1.024 caracteres; não vazia. A spec recomenda explicar o que faz e quando usar |
| `license` | não | nome da licença ou referência curta a arquivo incluído |
| `compatibility` | não | 1–500 caracteres; produto, ambiente, pacotes, rede ou outras exigências |
| `metadata` | não | mapa de chaves e valores string para extensões |
| `allowed-tools` | não | string com ferramentas pré-aprovadas; campo experimental e de suporte variável |

Exemplo mínimo completo:

```yaml
---
name: revisar-contrato
description: Use esta skill para revisar contratos e produzir uma matriz de riscos quando o usuário fornecer ou mencionar um documento contratual.
---

1. Leia o contrato inteiro e preserve a redação original das cláusulas citadas.
2. Para cada risco, informe cláusula, evidência, impacto e ação sugerida.
3. Se houver tratamento de dados pessoais, leia `references/privacidade.md`.
4. Entregue a matriz usando `assets/matriz-riscos.md` como estrutura.
```

Pedido “revise este contrato de fornecedor” → a `description` aparece no catálogo → o cliente
carrega este corpo → a referência de privacidade só entra se a condição ocorrer → o asset
define a forma do resultado. O pacote ensina o processo; leitura de arquivos, permissões e
ferramentas continuam a cargo do cliente.

O corpo não possui esquema obrigatório. Passos, exemplos de entrada e saída e casos-limite
são recomendações editoriais. Quando a skill ativa, o corpo inteiro entra no contexto.

### Duas bordas de interoperabilidade

1. A redação da especificação combina “alfanumérico Unicode” com exemplos `a-z` e `0-9`;
   a biblioteca de referência aceita alfabetos não latinos. **Inferência conservadora:**
   produzir nomes ASCII em `kebab-case` reduz divergência entre clientes.
2. A norma e o guia de descoberta usam o nome exato `SKILL.md`; o parser demonstrativo
   também tolera `skill.md`. Escrever estritamente e ler com tolerância é mais seguro.

### Recursos e referências

- `scripts/` contém código executável.
- `references/` contém documentação carregada quando necessária.
- `assets/` contém recursos estáticos usados no trabalho ou no resultado.
- Outros diretórios são válidos, mas seu significado não é interoperável por definição.
  `evals/`, por exemplo, é convenção do guia de avaliação, não parte obrigatória da spec.
- Caminhos referenciados partem da raiz da skill. A documentação recomenda referências a
  apenas um nível de profundidade para evitar cadeias difíceis de descobrir.
- Manter `SKILL.md` abaixo de 500 linhas é recomendação de contexto, não critério de validade.

## 3 · O que o padrão define — e o que deixa para o cliente

| O padrão define | O cliente ou ecossistema decide |
|---|---|
| anatomia da pasta e de `SKILL.md` | diretórios de instalação e descoberta |
| campos e limites do frontmatter | catálogo em XML, JSON, prompt ou ferramenta |
| corpo Markdown como instrução | ativação implícita, explícita ou ambas |
| recursos relativos à raiz | linguagens, runtimes e resolução de dependências |
| progressive disclosure como arquitetura | permissões, consentimento, sandbox e isolamento |
| convenções de `scripts/`, `references/`, `assets/` | instalação, registry, assinatura, atualização e lockfile |

`.agents/skills/` é uma convenção amplamente adotada para interoperabilidade, não requisito
do formato. `.claude/skills/`, diretórios do Codex e outros caminhos são escolhas de produto.
Da mesma forma, `/nome-da-skill` e `$nome-da-skill` são interfaces possíveis, não sintaxe
universal.

Não existe no contrato atual uma semântica normativa para composição entre skills, versão,
dependências, assinatura, registry ou política de confiança. Esses campos ou mecanismos podem
existir em um cliente, mas não viajam com garantia apenas por o pacote ser “Agent Skills”.

## 4 · Sob o capô: como um cliente implementa o ciclo

O [guia para implementadores](https://agentskills.io/client-implementation/adding-skills-support),
orientação oficial que não adiciona requisitos à spec, organiza cinco passos. Quem quer
primeiro criar uma skill pode seguir para a seção 5 e voltar aqui depois.

### 4.1 Descobrir

Clientes locais costumam procurar skills em dois escopos:

- **projeto:** capacidades específicas do repositório;
- **usuário:** capacidades disponíveis em todos os projetos.

Podem existir escopos da organização e skills embutidas. O guia sugere considerar tanto o
diretório nativo do produto quanto `.agents/skills/`. Em colisões, projeto vence usuário; no
mesmo escopo, a regra pode variar, mas deve ser determinística e gerar aviso.

Uma pasta de projeto recém-clonada pode ser hostil. O guia recomenda um portão de confiança
antes de permitir que instruções do repositório entrem silenciosamente no contexto.

### 4.2 Interpretar

O cliente extrai `name`, `description`, localização e corpo. A orientação é escrever de forma
estrita, mas ser tolerante na leitura quando possível: avisar e carregar problemas cosméticos;
ignorar a skill se a `description` faltar ou se o YAML for ininterpretável.

### 4.3 Expor o catálogo

O modelo recebe as skills disponíveis sem seus corpos completos. O catálogo pode ficar no
system prompt ou na descrição de uma ferramenta dedicada. Skills desabilitadas ou sem
permissão devem desaparecer do catálogo; catálogo vazio deve ser omitido.

### 4.4 Ativar

Duas estratégias são comuns:

- o modelo lê diretamente o arquivo pela ferramenta de arquivos;
- uma ferramenta `activate_skill` devolve o corpo, lista recursos e aplica permissões.

A ativação implícita costuma ser decisão do próprio modelo, não um regex do harness. O usuário
também deve poder acionar explicitamente. O modelo pode receber o arquivo inteiro ou apenas o
corpo sem frontmatter; ambos aparecem em implementações reais.

### 4.5 Preservar no tempo

Após ativada, a instrução precisa sobreviver à compactação de contexto. O cliente deve evitar
reinjeção duplicada e pode executar workflows complexos em subagente isolado. Se o conteúdo
da skill for resumido para fora do contexto no meio da tarefa, o desempenho degrada sem erro
visível.

## 5 · A `description` é um classificador em linguagem natural

O guia de [otimização de descriptions](https://agentskills.io/skill-creation/optimizing-descriptions)
trata o campo como o mecanismo primário de roteamento.

Uma boa descrição:

- usa formulação imperativa: “Use esta skill quando...”;
- descreve a intenção do usuário, não a implementação interna;
- inclui formas indiretas pelas quais a necessidade aparece;
- nomeia a fronteira com capacidades vizinhas;
- é específica o bastante para evitar falsos positivos e ampla o bastante para evitar
  falsos negativos;
- continua concisa, porque todas as descriptions ocupam o catálogo.

Há dois erros simétricos:

| Erro | Sintoma | Correção |
|---|---|---|
| estreita demais | tarefas úteis não acionam | ampliar intenções, formatos e contextos equivalentes |
| ampla demais | skill entra em quase-acertos e rouba contexto | declarar escopo e vizinhos negativos |

Mesmo uma descrição textual perfeita não torna o acionamento determinístico. O modelo pode
resolver uma tarefa simples sem consultar a skill; modelos e execuções diferentes podem tomar
decisões diferentes. Isso qualifica [description-como-gatilho](../conceitos/description-como-gatilho.md): é um gatilho probabilístico,
mensurável por taxa, e não uma regra booleana garantida pelo padrão.

No exemplo, “revise os riscos deste contrato” deve acionar; “converta este contrato de PDF para
Markdown” é um quase-negativo, porque manipula o mesmo arquivo mas pede outro job.

### Eval de acionamento

1. Criar cerca de 20 consultas: 8–10 que devem e 8–10 que não devem acionar.
2. Variar formalidade, erros, detalhes, caminhos, contexto pessoal e explicitude.
3. Usar negativos “quase certos”, que compartilham vocabulário mas pedem outro job.
4. Rodar cada consulta cerca de três vezes.
5. Medir taxa de acionamento; 0,5 é um limiar inicial sugerido, não lei universal.
6. Separar aproximadamente 60% para treino e 40% para validação.
7. Ajustar apenas pelas falhas de treino; escolher a versão pela validação.
8. Encerrar com 5–10 consultas inéditas.

Cinco iterações costumam ser suficientes. Estagnação pode indicar queries ou rótulos ruins,
não apenas uma description ruim.

## 6 · Como criar uma skill que acrescente capacidade real

O [guia de boas práticas](https://agentskills.io/skill-creation/best-practices) começa antes
do Markdown: uma skill boa nasce de expertise real.

```text
tarefa real ou artefatos reais
→ passos, correções, formatos e gotchas observados
→ unidade coerente de trabalho
→ instrução enxuta + recursos roteados
→ execução real
→ leitura dos rastros
→ revisão
```

Fontes férteis incluem runbooks, especificações, schemas, histórico de versões, comentários
de revisão, incidentes e resoluções. Uma LLM sem esse material tende a produzir generalidades
que já estavam em seu treinamento e pouco mudam o resultado.

### Escopo: a menor unidade coerente, não a menor unidade imaginável

Skills amplas demais acionam imprecisamente e carregam instruções irrelevantes. Skills estreitas
demais obrigam várias ativações, aumentam overhead e podem criar instruções conflitantes. A
recomendação oficial tensiona uma leitura literal de [skills-atomicas-componiveis](../conceitos/skills-atomicas-componiveis.md): “atômica”
deve significar **um job coerente e componível**, não fragmentar cada microcritério.

### Como gastar contexto

- Ensinar o que o modelo não saberia: convenções locais, procedimentos específicos, APIs,
  formatos e exceções não óbvias.
- Cortar definições genéricas e teoria que não muda comportamento.
- Preferir detalhe moderado, passos e um exemplo funcional à cobertura exaustiva.
- Manter no corpo apenas o que toda execução precisa; rotear detalhes condicionais.
- Dar default claro e alternativa como escape, não um menu de opções equivalentes.
- Ensinar procedimento reutilizável, não a resposta de uma única instância.

### Calibrar controle pela fragilidade

Explique intenção e permita julgamento quando várias abordagens são aceitáveis. Seja prescritivo
quando a operação é frágil, a ordem importa ou consistência é requisito. Uma mesma skill pode
misturar liberdade na análise e rigidez na migração ou validação.

### Padrões de instrução de alto valor

- **Gotchas:** fatos locais que corrigem uma suposição razoável do agente.
- **Templates:** forma concreta do output, inline ou em `assets/`.
- **Checklists:** estado visível em workflows com dependências.
- **Loop de validação:** fazer → validar → corrigir → repetir.
- **Planejar–validar–executar:** plano intermediário conferido contra fonte de verdade antes
  de ação em lote ou destrutiva.
- **Scripts reutilizáveis:** lógica que o agente reinventa em várias execuções vira código
  testado uma vez.

## 7 · Scripts: determinismo com uma interface para agentes

Um comando pontual é suficiente quando uma ferramenta existente resolve o job com poucos
argumentos. O guia recomenda mover comandos complexos, frágeis ou repetidos para `scripts/`;
a tabela abaixo é uma síntese operacional dessas orientações.

O guia mostra `uvx`, `pipx`, `npx`, `bunx`, `deno run` e `go run`, além de dependências inline
em Python/PEP 723, Deno, Bun e Ruby. Isso são opções, não runtimes garantidos. Versões devem ser
fixadas e requisitos declarados em `compatibility` quando relevantes.

### Contrato de um script amigável a agentes

| Propriedade | Por que importa |
|---|---|
| não interativo | o agente não responde a TTY, senha ou menu bloqueante |
| `--help` conciso | revela flags, formatos e exemplos sem adivinhação |
| erro acionável | informa problema, valor recebido, expectativa e próximo passo |
| saída estruturada | JSON/CSV/TSV pode ser composta e verificada |
| stdout limpo, stderr diagnóstico | separa dados de progresso e warnings |
| idempotência | retry não duplica ou corrompe estado |
| entrada fechada | rejeita ambiguidade em vez de inventar |
| `--dry-run` | antecipa efeitos de operação destrutiva ou stateful |
| exit codes significativos | permite reação diferente por tipo de falha |
| defaults seguros | reduz dano quando parâmetros faltam |

Isso converge com [skill-deterministica-hibrida-aberta](../conceitos/skill-deterministica-hibrida-aberta.md): a IA decide onde julgamento cria
valor; scripts e assets fixam o que precisa ser repetível. `allowed-tools` pode informar
pré-aprovação em alguns clientes, mas é experimental e não constitui sandbox universal.

## 8 · Síntese: avaliar em camadas, sempre contra um baseline

| Camada | Pergunta | Evidência |
|---|---|---|
| estrutura | o pacote obedece ao formato? | parser/validador |
| acionamento | entra nas tarefas certas e fica fora das erradas? | trigger rate positivo e negativo |
| resultado | melhora o trabalho comparado ao baseline? | assertions, artefatos e delta |
| revisão humana | resolve o problema e faz sentido? | feedback específico |
| segurança | origem, scripts, permissões e efeitos são aceitáveis? | revisão e controles do ambiente |

O guia de [avaliação de qualidade](https://agentskills.io/skill-creation/evaluating-skills)
recomenda começar com 2–3 casos realistas. Cada caso contém prompt, resultado esperado e
arquivos opcionais. Execute-o em contexto limpo **com a skill e sem ela**; ao revisar uma skill
existente, use a versão anterior como baseline.

Depois de ver os primeiros outputs:

1. escrever assertions específicas e observáveis;
2. verificar mecanicamente o que for possível e usar julgamento para qualidades difíceis;
3. exigir evidência concreta para cada PASS;
4. registrar tokens e duração;
5. agregar taxa de sucesso, custo e dispersão;
6. ler os rastros, não apenas a resposta final;
7. colher feedback humano acionável;
8. generalizar correções e repetir a rodada completa.

No exemplo, uma assertion observável seria: “cada risco contém cláusula, evidência, impacto e
ação”. Compare a taxa de atendimento com e sem a skill; a mera presença do título “Matriz de
riscos” não basta para PASS.

Assertions que passam com e sem a skill não provam valor. Falhas em ambos podem revelar teste
quebrado ou capacidade inviável. Ganhos pequenos com grande custo contextual podem não
justificar o pacote. O loop termina quando o feedback fica vazio, o resultado satisfaz ou as
iterações deixam de produzir melhoria relevante.

### O alcance real de `skills-ref`

A biblioteca oficial demonstrativa oferece `validate`, `read-properties` e `to-prompt`.
Ela verifica estrutura e metadados; não prova qualidade do corpo, acionamento, links,
segurança de scripts ou benefício do output. Seu README a identifica como demonstração,
não ferramenta de produção. Na versão examinada era `0.1.0`.

**Inferência:** a spec dá um lint, não uma certificação. Uma skill válida pode ser inútil,
perigosa ou invisível; as outras camadas de avaliação continuam necessárias.

## 9 · Inferência de segurança: instalar uma skill se parece mais com instalar código

Uma skill contém instruções que entram no contexto e pode conter código executável. Portanto,
proveniência e confiança importam mesmo quando o pacote parece “só Markdown”.

Checklist mínimo proposto neste estudo:

- revisar origem, licença e histórico;
- inspecionar corpo, scripts, dependências e assets;
- desconfiar de skills de projetos recém-clonados;
- limitar ferramentas e diretórios ao necessário;
- exigir preview e confirmação proporcional ao risco;
- proteger segredos e dados sensíveis;
- testar idempotência e efeitos colaterais;
- manter a versão usada sob controle de versão.

A especificação não define assinatura, registry confiável, sandbox, resolução de dependências
ou consentimento. O guia de cliente recomenda trust gate e allowlist, mas a eficácia depende
do harness. Portabilidade não transfere automaticamente a política de segurança.

## 10 · Ecossistema e governança no snapshot

O formato nasceu na Anthropic e foi aberto para contribuição no repositório
`agentskills/agentskills`. Código e especificação usam Apache 2.0; documentação usa CC BY 4.0.
O projeto declarava o núcleo ainda em evolução, sem tag ou release formal no snapshot. A
barreira de contribuição privilegia problemas observados em implementações reais e evita
ampliar a especificação sem necessidade.

O showcase dinâmico listava 44 clientes em 2026-07-21, entre eles Claude, Claude Code,
OpenAI Codex, GitHub Copilot, VS Code, Cursor, Gemini CLI, OpenCode, Databricks e Snowflake.
A lista integral é acessível pelo permalink datado em [agent-skills-open-standard](../fontes/agent-skills-open-standard.md).

Para entrar na vitrine, o produto deve estar público, já descobrir e executar skills e mostrar
documentação. Isso é um filtro de existência, não teste de equivalência. Caminhos, parsing,
ativação, ferramentas, permissões, compactação e modelos continuam variáveis.

## 11 · Distinção entre o padrão e convenções de implementação

| Elemento | Estado |
|---|---|
| pasta + `SKILL.md` | núcleo do padrão aberto |
| `name` + `description` | contrato normativo e catálogo |
| `scripts/`, `references/`, `assets/` | diretórios opcionais convencionais da spec |
| `.agents/skills/` | convenção interoperável, não requisito |
| `.claude/skills/` | compatibilidade específica de clientes |
| `agents/openai.yaml` | camada local de apresentação no Codex, fora do padrão |
| `INGEST.md` e `sources/` | protocolo adicional de evolução e proveniência, permitido mas não padronizado |
| skills personificadas | aplicação local do formato, não categoria da especificação |
| reiniciar ao criar skill | comportamento de implementação, não regra universal |

### Convergências

- [skill-de-agente](../conceitos/skill-de-agente.md) acerta ao tratar a skill como pacote de instrução, contexto e recursos.
- [description-como-gatilho](../conceitos/description-como-gatilho.md) corresponde ao catálogo da divulgação progressiva.
- [engenharia-reversa-para-skills](../conceitos/engenharia-reversa-para-skills.md) converge com partir de tarefa e artefatos reais.
- travas-nascem-de-falhas converge com transformar correções e rastros em gotchas.
- [skill-deterministica-hibrida-aberta](../conceitos/skill-deterministica-hibrida-aberta.md) converge com empacotar scripts repetíveis.
- O padrão “roteador + referências sob demanda” aplica a arquitetura central do site.

### Tensões úteis

- A documentação oficial prefere uma unidade **coerente**: estreita demais também é defeito.
- `.agents/skills/` favorece portabilidade, mas o padrão não exige qualquer caminho.
- Descrição explícita melhora a chance de ativação, mas o julgamento continua probabilístico.
- Um `SKILL.md` grande pode ser válido e ainda degradar atenção e custo.
- Um pacote sintaticamente válido não demonstra segurança nem benefício.
- `INGEST.md`, `sources/` e `agents/openai.yaml` são extensões funcionais possíveis; não
  devem ser ensinadas como exigências universais.

## 12 · Síntese: checklist integrado de criação

Este não é um checklist normativo da especificação.

1. **Prove o job:** existe tarefa recorrente em que o agente erra ou carece de contexto?
2. **Parta do real:** reúna execução, correções, artefatos, edge cases e formatos verdadeiros.
3. **Defina a unidade:** um job coerente, com vizinhos e não-escopo explícitos.
4. **Escreva o catálogo:** `name` portátil e `description` orientada à intenção.
5. **Escreva o núcleo:** apenas o procedimento e os gotchas necessários em toda execução.
6. **Roteie o detalhe:** diga condição e caminho exatos de cada referência.
7. **Empacote certeza:** scripts para lógica repetida; assets para material estático.
8. **Declare ambiente:** `compatibility`, versões e pré-requisitos quando necessários.
9. **Valide estrutura:** parser/lint estrito antes de testar comportamento.
10. **Teste o trigger:** positivos, quase-negativos, repetições e validação separada.
11. **Teste o resultado:** com/sem skill, assertions, custo, rastros e revisão humana.
12. **Revise segurança:** confiança, código, permissões, segredos e efeitos colaterais.
13. **Teste portabilidade:** clientes realmente necessários, não um “compatível” abstrato.
14. **Itere por evidência:** cortar também é melhoria; parar quando o ganho marginal some.

## Conclusão

Agent Skills é menos um “prompt salvo” e mais uma arquitetura de **contexto endereçável**:
catálogo leve, procedimento carregável e recursos sob demanda. Sua força está em tornar
expertise versionável, auditável e transportável. Sua fronteira é igualmente importante:
o formato não substitui um bom cliente, um modelo capaz, testes, permissões ou julgamento
humano. A melhor skill é a menor unidade coerente que melhora um resultado observável com
custo e risco aceitáveis. Próximos testes úteis são auditar uma skill, comparar resultados com e sem a skill e executar a mesma pasta nos clientes necessários.
