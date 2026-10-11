# Agent Skills: fontes públicas do padrão aberto

## Escopo preservado

Ponteiro composto para o site e o repositório oficiais do **Agent Skills**, formato aberto
originalmente desenvolvido pela Anthropic para empacotar conhecimento e workflows de
agentes. A ficha original registra leitura do corpus em 2026-07-21. Trata-se da procedência daquele levantamento, sem alegar atualização normativa nesta publicação.

O snapshot consultado do repositório `agentskills/agentskills` estava no commit
[`38a2ff8`](https://github.com/agentskills/agentskills/commit/38a2ff82958afee88dadf4831509e6f7e9d8ef4e),
com timestamp UTC de 2026-07-10. A última alteração da especificação naquele histórico era
de 2026-05-16. Não havia tag ou release formal do padrão; por isso a data e o commit fazem
parte da proveniência.

## Corpus oficial lido

- [Índice para LLMs](https://agentskills.io/llms.txt) — enumera o corpus documental.
- [Visão geral](https://agentskills.io/home) — propósito, estrutura e modelo de carregamento.
- [Especificação](https://agentskills.io/specification) — contrato do formato.
- [Quickstart](https://agentskills.io/skill-creation/quickstart) — primeira skill funcional.
- [Boas práticas](https://agentskills.io/skill-creation/best-practices) — escopo, contexto e
  padrões de instrução.
- [Otimização de descriptions](https://agentskills.io/skill-creation/optimizing-descriptions) —
  avaliação do acionamento.
- [Avaliação de qualidade](https://agentskills.io/skill-creation/evaluating-skills) — baseline,
  assertions, grading e iteração.
- [Uso de scripts](https://agentskills.io/skill-creation/using-scripts) — desenho de comandos e
  scripts para agentes.
- [Implementação em clientes](https://agentskills.io/client-implementation/adding-skills-support) —
  descoberta, ativação, confiança e gestão de contexto.
- [Showcase de clientes](https://agentskills.io/clients) — vitrine dinâmica dos produtos
  compatíveis.
- [Repositório da especificação](https://github.com/agentskills/agentskills) — documentação,
  histórico, contribuição e implementação de referência.
- [`skills-ref`](https://github.com/agentskills/agentskills/blob/38a2ff82958afee88dadf4831509e6f7e9d8ef4e/skills-ref/README.md) —
  biblioteca demonstrativa de leitura e validação; o próprio README diz que não é destinada
  à produção.
- [Exemplos da Anthropic](https://github.com/anthropics/skills) — implementações ilustrativas,
  não parte normativa do padrão e com licenças que devem ser verificadas individualmente.

## Proveniência e limites

- O [código e a especificação](https://github.com/agentskills/agentskills/blob/38a2ff82958afee88dadf4831509e6f7e9d8ef4e/LICENSE)
  declaram licença Apache 2.0; a [documentação](https://github.com/agentskills/agentskills/blob/38a2ff82958afee88dadf4831509e6f7e9d8ef4e/docs/LICENSE),
  CC BY 4.0.
- O showcase era alimentado pelo snapshot de
  [`clients.jsx`](https://github.com/agentskills/agentskills/blob/38a2ff82958afee88dadf4831509e6f7e9d8ef4e/docs/snippets/clients.jsx)
  e listava 44 clientes. É evidência de adoção naquele momento, não certificação de
  comportamento idêntico.
- O projeto exige que um produto esteja público e já descubra e execute skills para entrar
  no showcase, mas não oferece uma suíte formal de conformidade.
- A especificação define o conteúdo do pacote. Instalação, distribuição, permissões,
  sandbox, runtime e semântica exata de ativação continuam dependentes do cliente.

## Materiais incluídos nesta coleção

- Estudo e síntese: [agent-skills-padrao-aberto-estudo](../estudos/agent-skills-padrao-aberto-estudo.md).
- Entrada de navegação neutra: agent-skills-moc.
- Conceito canônico atualizado e separado das convenções locais: [skill-de-agente](../conceitos/skill-de-agente.md).
