# 02 — Anatomia do prompt (modo CRIAR)

Carregue no MODO CRIAR: montar o prompt — elementos, delimitadores, contrato de saída, template mestre.

## O insight central

Um prompt bem construído tem **4 elementos** (taxonomia do Prompt Engineering Guide/DAIR.AI): **instrução** (o que fazer), **contexto** (informação que orienta), **dados de entrada** (o material da tarefa) e **indicador de saída** (formato/começo da resposta). A maioria dos prompts fracos tem instrução vaga, contexto misturado com dados e saída sem contrato. Separar é 80% do conserto.

## O protocolo de construção

1. **Objetivo em 1 frase.** Se você não consegue, o modelo também não. ("Gerar plano de mensuração pra e-commerce, público analista júnior, ≤600 palavras.")
2. **Papel e âmbito** (se agrega): "Atue como [função] com foco em [área]" + escopo incluído/excluído. Papel sem função é cosplay; papel com escopo corta divagação.
3. **Separe instrução de dados** com delimitadores — tags XML são o padrão de produção (`<instrucoes>`, `<dados>`, `<exemplos>`): endereçáveis, aninháveis e o modelo respeita as fronteiras.
4. **Contrato de saída** (o coração): estrutura (seções/JSON/tabela), campos obrigatórios, critérios de qualidade, formato de entrega. + Cláusula de parada: *"se faltar informação crítica, liste exatamente o que falta e pare."*
5. **Exemplos, se o formato for difícil de descrever** (2–5, formato rigorosamente consistente — Min et al.: o formato é o que ensina). Inclua um caso-limite.
6. **Instruções críticas perto do fim** ([[fim-do-prompt-tem-mais-peso]]); dados volumosos no meio.
7. **Passe anti-negativas:** reescreva cada "não faça X" como "faça Y".

## Heurísticas / regras

- Especificidade vence tamanho: prompt curto e específico > longo e vago. Mas não confunda com o mito do prompt curto — se a tarefa tem casos-limite, eles precisam estar lá.
- Um prompt, uma tarefa. Duas tarefas = chaining (`04`).
- Temperatura: exatidão/extração → baixa; criação → alta. Mexa em temperatura OU top-p, não ambos.
- Itere: primeira versão → teste em 3 casos reais → ajuste onde falhou. Prompt é rascunho até passar no teste.

## O template mestre (pra instrução reutilizável)

Quando o prompt for reutilizável/mestre, use este esqueleto de 12 seções: objetivo & contexto · papel & âmbito · estilo & tom · ferramentas/fontes/citações · artefatos · memória · entradas · **saída esperada** · processo · **checklist de qualidade** · diretrizes específicas · limitações & recusas — + bloco de execução variável por chamada. Pra prompt pontual, use só §1, §2, §7, §8 e o bloco de execução.

## Como entregar

1. Entregue o prompt completo em bloco copiável, com os delimitadores já no lugar.
2. Aponte as 2–3 decisões que importam ("contrato de saída em JSON porque você vai parsear; exemplo do caso-limite X porque é onde modelos erram").
3. Feche com o teste: "roda nesses 3 casos; me traz o pior resultado que eu ajusto".

## Conexões

- Tarefa de raciocínio → adicione o degrau de `03`. Conhecimento/tools → `04`. Se virar system prompt → `05`. Pra revisar o que você criou → checklist de `06`.

<!-- fontes: prompt-engineering-guide-dair, rafael-template-mestre-de-prompt, min-rethinking-demonstrations (notas de curadoria), ingerido em 2026-07-05. Atualize via INGEST.md -->
