# ART: Automatic multi-step reasoning and tool-use for large language models

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [ART: Automatic multi-step reasoning and tool-use for large language models](https://arxiv.org/abs/2303.09014).

Paranjape et al. (UW/Microsoft/Meta, 2023) apresentam o ART, framework frozen-LLM que, dada uma tarefa nova, **seleciona automaticamente demonstrações de raciocínio multi-step e uso de ferramentas de uma task library**, gera o programa de raciocínio, pausa a geração para chamar tools externas (busca, calculadora, código) e retoma integrando o resultado. Zero fine-tuning: iguala ou supera CoT feito à mão em BigBench e MMLU, e é extensível — humanos podem editar a library para corrigir erros. Conceito relacionado: [ART — Automatic Reasoning and Tool-use](../conceitos/art-automatic-reasoning-tool-use.md).
