# Meta Prompting for AI Systems

> Ficha metodológica registrada em 2026-07-05. Síntese histórica; não reproduz o texto integral da fonte.

Fonte pública: [Meta Prompting for AI Systems](https://arxiv.org/abs/2311.11482).

Zhang et al. (2023) formalizam o **meta prompting**: priorizar a *estrutura e a sintaxe* do problema (template, formato, esqueleto de raciocínio) em vez de exemplos ricos em conteúdo — o oposto do few-shot tradicional. Fundamentado em teoria de categorias/type theory, inclui o **Meta Prompting for Prompting Tasks** (o LLM escreve/revisa os próprios prompts, funcionando como meta-programação em linguagem natural) e mostra eficiência de tokens e comparação mais justa entre modelos por ser essencialmente zero-shot; reporta resultados fortes como 46.3% no MATH e 83.5% no GSM8K com Qwen-72B. Conceito relacionado: [Meta-prompting](../conceitos/meta-prompting.md).
