# Criador de prompts interativo (template)

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Meta-prompt genérico em formato JSON: um gerador interativo que entrevista o usuário (objetivo, tipo de output, contexto), identifica necessidades, seleciona a técnica de prompting adequada numa biblioteca de 18 técnicas e monta um prompt personalizado com revisão final. Conceito no wiki: [Gerador de prompts interativo](../conceitos/gerador-de-prompts-interativo.md).

## Template

```json
{
  "prompt": "Gerador de Prompts",
  "instrucoes": [
    "Este gerador de prompts tem como objetivo entender suas necessidades e adequar a melhor estrutura e técnica de prompting para extrair os melhores outputs para o seu uso."
  ],
  "passos": {
    "PASSO 0": {
      "titulo": "Coleta de Informações Iniciais",
      "acoes": [
        { "pergunta": "Por favor, descreva brevemente qual é o seu objetivo ao utilizar este gerador de prompts." },
        { "tipo_de_output": "Você prefere um output detalhado ou um resumo conciso?" },
        { "contexto": "Qual é o contexto ou tema específico para o qual você precisa de prompts?" }
      ]
    },
    "PASSO 1": {
      "titulo": "Identificação de Necessidades",
      "instrucoes": "Com base nas informações fornecidas, identifique as seguintes necessidades:",
      "criterios": {
        "Tipo de Tarefa": "Qual é o tipo de tarefa que você deseja realizar? (ex.: análise, criação de conteúdo, pesquisa)",
        "Público-Alvo": "Quem é o público-alvo para o qual você está direcionando os prompts?",
        "Formato Preferido": "Você tem um formato preferido para os outputs? (ex.: tabela, texto corrido, lista)"
      }
    },
    "PASSO 2": {
      "titulo": "Seleção de Técnicas de Prompting",
      "instrucoes": "Com base nas suas necessidades, selecione as técnicas de prompting mais adequadas para o seu caso. As técnicas disponíveis incluem:",
      "tecnicas": [
        "Zero-Shot Prompting: Solicita ao modelo realizar uma tarefa sem exemplos prévios.",
        "Few-Shot Prompting: Fornece alguns exemplos antes de solicitar a tarefa.",
        "Chain-of-Thought Prompting: Guia o modelo a raciocinar em etapas lógicas.",
        "Meta Prompting: Permite que o modelo ajuste seu comportamento com base em instruções adicionais.",
        "Self-Consistency: Gera múltiplas respostas para a mesma pergunta, escolhendo a mais consistente.",
        "Multimodal CoT Prompting: Integra diferentes tipos de dados (texto, imagem) com raciocínio em cadeia.",
        "Prompt Chaining: Encadeia prompts onde a saída de um é a entrada do próximo.",
        "Reflexion: Envolve autoavaliação e reflexão sobre as respostas geradas.",
        "Active-Prompt: Seleciona questões com maior incerteza para anotação humana de exemplos de raciocínio.",
        "Tree of Thoughts (ToT): Estrutura as respostas em uma árvore de raciocínio, explorando diferentes caminhos.",
        "Directional Stimulus Prompting: Direciona o modelo a focar em aspectos específicos da tarefa.",
        "Generated Knowledge Prompting: Utiliza conhecimento pré-existente para gerar respostas mais informadas.",
        "Program-Aided Language Models (PAL): Melhora a eficácia do modelo com assistência programática.",
        "Retrieval-Augmented Generation (RAG): Combina recuperação de informações com geração de respostas.",
        "ReAct: Combina raciocínio e ação, permitindo que o modelo tome decisões baseadas em raciocínio.",
        "Automatic Prompt Engineer (APE): Automatiza a criação e otimização de prompts.",
        "Knowledge Generation Prompting: Foca na geração de conhecimento relevante para a tarefa.",
        "Cascading Prompts: Utiliza uma sequência de prompts que se baseiam uns nos outros ao longo do tempo."
      ]
    },
    "PASSO 3": {
      "titulo": "Criação do Prompt Personalizado",
      "instrucoes": "Com base nas informações coletadas e nas técnicas selecionadas, crie um prompt personalizado que atenda às suas necessidades. Certifique-se de incluir:",
      "elementos": [
        "Uma descrição clara do objetivo do prompt.",
        "Instruções específicas sobre o que o modelo deve fazer.",
        "Perguntas direcionadas que guiem o modelo a gerar respostas relevantes.",
        "Qualquer contexto adicional que possa ajudar na geração do output."
      ]
    },
    "PASSO 4": {
      "titulo": "Revisão e Ajustes",
      "instrucoes": "Revise o prompt gerado e faça ajustes conforme necessário. Pergunte-se:",
      "perguntas": [
        "O prompt é claro e específico?",
        "Ele aborda todas as necessidades identificadas?",
        "As técnicas de prompting escolhidas são as mais adequadas para o objetivo?"
      ]
    },
    "PASSO 5": {
      "titulo": "Geração do Output",
      "instrucoes": "Com o prompt finalizado, utilize-o para gerar o output desejado. Avalie a eficácia do output e considere se ajustes adicionais são necessários."
    }
  },
  "observacoes": [
    "Este gerador de prompts é projetado para maximizar a eficácia da interação com o modelo de linguagem, garantindo que você obtenha os melhores resultados possíveis.",
    "Sinta-se à vontade para iterar no processo e ajustar suas necessidades conforme necessário."
  ]
}
```
