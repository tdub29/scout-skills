# Logic-LM Reference

Pan et al., "Logic-LM: Empowering Large Language Models with Symbolic Solvers" (EMNLP 2023)

Source: https://github.com/teacherpeterpan/Logic-LLM

## Pipeline

```
NL Problem â†’ LLM (few-shot) â†’ Logic Program â†’ Symbolic Solver â†’ Answer
                   â†‘                               |
                   â””â”€â”€â”€â”€ Self-Refinement â†â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                              (on errors)
```

## Dataset-Solver Mapping

| Dataset | Logic Type | Solver | Answer Format |
|---------|------------|--------|---------------|
| FOLIO | First-order logic | Prover9 | True/False/Unknown |
| ProntoQA | Propositional | Pyke | True/False |
| ProofWriter | Propositional | Pyke | True/False |
| LogicalDeduction | Constraints | CSP | A/B/C/D/E |
| AR-LSAT | Satisfiability | Z3 | A/B/C/D/E |

## Logic Program Format

Programs use `:::` to annotate each line with natural language explanation.

**FOL (FOLIO-style):**
```
Predicates:
PredicateName(x) ::: description

Premises:
âˆ€x (P(x) â†’ Q(x)) ::: description
P(constant) ::: description

Conclusion:
Q(constant) ::: description
```

**Constraints (AR-LSAT-style):**
```
# Declarations
sort_name = EnumSort([member1, member2, ...])
function_name: sort -> type

# Constraints
constraint_expression ::: description

# Options
(A): is_valid(expr) / is_sat(expr) / is_exception(expr)
```

See actual prompt templates in the repo: `models/prompts/`

## Self-Refinement

When solver returns an error, retry with the original program + error message. Max rounds: 3 (configurable).
