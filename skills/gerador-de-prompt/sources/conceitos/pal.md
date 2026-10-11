# PAL — Program-Aided Language Models

> Nota metodológica registrada em 2026-07-05. É uma síntese histórica das fontes citadas, sem nova validação de resultados.

**PAL (Program-Aided Language Models)** (Gao et al., 2022) é a técnica em que o LLM lê o problema e gera **um programa Python como passos intermediários de raciocínio**, delegando a execução ao interpretador — a resposta final vem do runtime, não do modelo.

A divisão de trabalho é a tese: o LLM faz o que faz bem — **entender o problema em linguagem natural e decompô-lo** — e o interpretador faz o que o LLM faz mal — **computar com exatidão**. No [Chain-of-Thought (CoT)](chain-of-thought.md) clássico, o modelo frequentemente decompõe certo mas erra a aritmética no meio do caminho; no PAL esse modo de falha desaparece porque a computação sai do processo estocástico e vai pro runtime determinístico. É a aplicação mais limpa de determinismo e variabilidade em prompting: raciocínio semântico estocástico, execução determinística.

Funciona como [Few-shot prompting](few-shot-prompting.md): as demonstrações mostram problemas resolvidos com código intercalado a comentários em linguagem natural. Com Codex, PAL bateu estado da arte few-shot no **GSM8K**, superando o PaLM-540B com CoT em ~15 pontos absolutos de acurácia top-1 — um modelo menor com interpretador venceu um modelo muito maior "de cabeça". Ganhos análogos em raciocínio simbólico e algorítmico (BIG-Bench Hard). Trabalho irmão e contemporâneo: PoT — Program of Thoughts (Chen et al., 2022).

O legado é visível em todo estrutura de execução de agentes atual: code interpreter, tool de execução de código e a filosofia "deixe o modelo escrever código em vez de simular computação" descendem diretamente daqui. No quadro geral, PAL é uma tool específica dentro do espectro que o [ReAct prompting (Reason + Act)](react-prompting.md) generaliza e que o [ART — Automatic Reasoning and Tool-use](art-automatic-reasoning-tool-use.md) automatiza.

## Conexões
determinismo e variabilidade · [Chain-of-Thought (CoT)](chain-of-thought.md) · [ReAct prompting (Reason + Act)](react-prompting.md) · [ART — Automatic Reasoning and Tool-use](art-automatic-reasoning-tool-use.md) · [Few-shot prompting](few-shot-prompting.md) · estrutura de execução de agentes · previsão do próximo token em transformers · [Engenharia de prompts](engenharia-de-prompts.md)

## Fontes
[PAL: Program-aided Language Models](../fontes/gao-pal.md)
