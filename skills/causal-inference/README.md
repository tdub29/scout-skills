# causal-inference

An opinionated [Agent Skill](https://agentskills.io) for production-grade Bayesian causal inference using [PyMC](https://www.pymc.io/welcome.html), [CausalPy](https://causalpy.readthedocs.io/en/stable/), and [DoWhy](https://www.pywhy.org/dowhy/v0.14/).

Compatible with Claude Code, Kimi Code, Cursor, Gemini CLI, and any agent that supports the [Agent Skills spec](https://agentskills.io/specification).

Full breakdown [here](https://learnbayesstats.com/blog-posts/causal-inference-agent-skill-pymc-causalpy-dowhy).

## What it does

Guides your coding agent through the full causal inference workflow, enforcing DAG-first thinking and mandatory assumption checkpoints:

1. **Formulate the causal question** â€” Precise estimand (ATE, ATT, LATE, etc.)
2. **Draw the DAG** â€” Explicit causal graph with nodes, edges, and non-edges
3. **Identify** â€” Backdoor, front-door, IV, RDD, DiD
4. **Choose design** â€” Match problem to method (DiD, synthetic control, ITS, RDD, IV, IPSW, structural)
5. **Estimate** â€” Build and fit the model (delegates PyMC mechanics to bayesian-workflow)
6. **Refute** â€” Mandatory design-specific robustness checks (placebo tests, sensitivity analysis, falsification)
7. **Interpret** â€” Effect size + decision-relevant HDIs + probability of direction
8. **Report** â€” Canonical `<treatment>-on-<outcome>/report.md` artifact with programmatic causal-language calibration

The skill enforces guardrails that agents won't apply on their own: no estimation without a confirmed DAG, adjustment licensed by the DAG rather than timing (pre-treatment covariates are necessary, not sufficient â€” M-bias still bites), no causal claims without refutation, assumptions stated before results, and a programmatic harness (`scripts/check_refutation.py`) that calibrates the report's causal language â€” causal / suggestive / associational / descriptive â€” directly from refutation outcomes, instead of leaving the call to human (or agent) judgment.

## Install

This skill requires the **bayesian-workflow** skill for all PyMC modeling steps (priors, sampling, diagnostics, calibration, reporting). Install both together.

### Claude Code

```bash
git clone https://github.com/Learning-Bayesian-Statistics/baygent-skills.git /tmp/baygent-skills
mkdir -p ~/.claude/skills
cp -r /tmp/baygent-skills/bayesian-workflow ~/.claude/skills/
cp -r /tmp/baygent-skills/causal-inference ~/.claude/skills/
```

For project-level installation (available only in that project), copy into `.claude/skills/` at the project root instead.

### Other compatible agents (Kimi Code, Cursor, etc.)

```bash
git clone https://github.com/Learning-Bayesian-Statistics/baygent-skills.git /tmp/baygent-skills
cp -r /tmp/baygent-skills/bayesian-workflow/ ~/.config/agents/skills/bayesian-workflow/
cp -r /tmp/baygent-skills/causal-inference/ ~/.config/agents/skills/causal-inference/
```

### Python dependencies

```bash
mamba install -c conda-forge pymc nutpie arviz arviz-stats causalpy dowhy
```

## Example prompts

Once installed, just ask your agent naturally:

- *"We ran a marketing campaign in 3 cities starting in March. I have monthly revenue data for those cities plus 10 control cities. Did the campaign work?"*
- *"I have observational data on a drug treatment. Help me estimate the causal effect controlling for confounders."*
- *"Does X cause Y? I have panel data with a treatment that rolled out at different times across regions."*
- *"I need to estimate the effect of a policy change using regression discontinuity â€” students above a test score threshold got a scholarship."*
- *"Build a synthetic control for California's tobacco tax using other states as donors."*

## Design selection guide

| Design | Use when | Tool |
|---|---|---|
| DiD | Treatment at known time, control group available | CausalPy |
| Staggered DiD | Treatment rolls out at different times | CausalPy |
| Synthetic Control | Single treated unit, donor pool available | CausalPy |
| ITS | Time series, intervention at known time, no control | CausalPy |
| RDD | Treatment by threshold on running variable | CausalPy |
| IV | Endogenous treatment, valid instrument | CausalPy |
| IPSW | Observational data, treatment modeled | CausalPy |
| Structural (do/observe) | Full causal theory, model mechanisms | PyMC |
| Counterfactual | "What would Y have been if X differed?" | PyMC |

## What's included

```
causal-inference/
â”œâ”€â”€ SKILL.md                          # Main workflow instructions
â”œâ”€â”€ references/
â”‚   â”œâ”€â”€ dags-and-identification.md    # DAG construction, backdoor/front-door criteria
â”‚   â”œâ”€â”€ quasi-experiments.md          # DiD, synthetic control, ITS, RDD, IV, IPSW
â”‚   â”œâ”€â”€ structural-models.md          # pm.do(), pm.observe(), counterfactuals
â”‚   â”œâ”€â”€ refutation.md                 # Design-specific robustness checks
â”‚   â””â”€â”€ reporting.md                  # Canonical report artifact + causal language guardrails
â””â”€â”€ scripts/
    â””â”€â”€ check_refutation.py           # Interprets refutation outcomes â†’ calibrated causal language + suggested next steps
```

## License

MIT - see [LICENSE](../LICENSE).
