# Dixit & Nalebuff â€” Dominance, Iterated Elimination, and Nash Equilibrium

## The framework

> The idea is to look for an outcome where each player in the game chooses the strategy that best serves his or her own interest, in response to the other's strategy. If such a configuration of strategies arises, neither player has any reason to change his choice unilaterally. (Chapter 4)

This is the toolkit for *simultaneous-move* games â€” players choose at the same time, each in ignorance of the others' current choice but aware that everyone is reasoning the same way. Because there is no "later node" to fold back, you cannot use backward reasoning (see `references/dixit-backward-reasoning-game-trees.md`). Instead you analyze **best responses**, **dominance**, and the **Nash equilibrium**.

### The payoff matrix

Lay the game out as a table: your strategies on the rows, the rival's on the columns, each cell holding both players' payoffs. A *best response* is the strategy that gives you the highest payoff *given a belief about what the other is choosing* â€” note that since moves are simultaneous you are responding to a **belief**, not to an observed move. Mark each player's best response to every possible choice of the other; the cells where both marks coincide are the candidate solutions.

### Dominant and dominated strategies â€” and iterated elimination

- A **dominant strategy** is best for you *no matter what* the other player does. If you have one, play it â€” no further reasoning about the other's choice is needed.
- A **dominated strategy** is one that is worse than some other strategy of yours *no matter what* the rival does. Never play a dominated strategy.
- **Iterated elimination of dominated strategies:** delete your dominated strategies; given that you would never play them, the rival can delete strategies that were only good responses to them; this may expose new dominated strategies for you; repeat. Sometimes this peels the game down to a single outcome.

### The prisoner's dilemma as an equilibrium

In the prisoners' dilemma, **Confess (defect) is a dominant strategy for each player**: "If one confesses, the other had better confess to avoid the really harsh sentence reserved for recalcitrants; if one holds out, the other can cut himself a much better deal by confessing" (Ch 3). So both confess â€” even though both would do better staying silent. The dilemma is the canonical case where dominance leads each rational player to a jointly *bad* equilibrium. Dixit & Nalebuff show the same structure in price wars (two gas stations), centrist campaign convergence, overfished commons, and Yossarian's logic in *Catch-22*. Tucker invented the prisoners'-dilemma *story* in 1950 to dramatize "Nash equilibria and the attendant paradoxes of non-socially-desirable equilibria."

### Nash equilibrium

When no player has a dominant strategy â€” each one's best choice depends on the other's (the Stone Age stag/bison hunters Fred and Barney) â€” you square the circle of "thinking about thinking about thinking" with John Nash's concept:

> A **Nash equilibrium** is a configuration of strategies, one per player, such that each player's strategy is a best response to the others' â€” so **no player can do better by unilaterally changing his own strategy.**

It is a *potentially stable* outcome and the recommended **starting point for analyzing almost any game**. Caveats the book stresses: a game may have **no** pure-strategy Nash equilibrium (then look for a mixed one â€” see `references/dixit-mixing-strategies.md`), or **several** (chicken and the stag hunt each have two â€” then the question becomes which one the players coordinate on; see `references/dixit-coordination-vs-dilemma.md` and `references/schelling-focal-points.md`).

## How to apply

1. **Confirm the game is simultaneous** (players move blind and at once). If they move in observable sequence, use backward reasoning instead.
2. **Build the payoff matrix.** Name the players, their discrete strategy choices, and a payoff number (or ranking) for each player in each cell.
3. **Check for dominance first** â€” it is the cheapest reasoning. If you have a dominant strategy, play it. Delete any dominated strategies for both sides and iterate.
4. **If dominance does not solve it, find the Nash equilibria.** Mark each player's best response to each of the other's choices; cells where best responses coincide are equilibria.
5. **Interpret the equilibrium.** Is it unique or multiple? Is it socially good or a dilemma? A dilemma is a signal to look for ways to *change the game* (repetition, enforcement, commitment) â€” handoff to the coordination/dilemma and credibility references.

## Common failure modes

- **Calling a dominant-strategy outcome "irrational."** In the prisoners' dilemma each player is acting rationally; the dilemma is structural, not a failure of reasoning. Fixing it requires changing payoffs, not lecturing the players.
- **Assuming a unique equilibrium.** Chicken and assurance games have multiple; declaring "the" equilibrium without checking hides the real (coordination) problem.
- **Forgetting the no-pure-equilibrium case.** Zero-sum "matching" games (penalty kicks) have no pure Nash equilibrium; the solution is mixed.
- **Responding to the move instead of the belief.** Moves are simultaneous â€” you optimize against your *belief* about the rival's choice, formed from reasoning, experience, or guesswork.
- **Treating a repeated game as one-shot.** The dominant-strategy logic of the *single* prisoners' dilemma can flip when the game repeats (see `references/axelrod-tit-for-tat-repeated-games.md`).

## References

- Avinash Dixit & Barry Nalebuff, *The Art of Strategy* (W. W. Norton, 2008), Chapter 3, "Prisoners' Dilemmas and How to Resolve Them," and Chapter 4, "A Beautiful Equilibrium" (dominance, best responses, Nash equilibrium; Tucker's 1950 story).
- Related: [references/dixit-backward-reasoning-game-trees.md](references/dixit-backward-reasoning-game-trees.md) (sequential counterpart), [references/dixit-coordination-vs-dilemma.md](references/dixit-coordination-vs-dilemma.md) (multiple-equilibrium and dilemma structures), [references/dixit-mixing-strategies.md](references/dixit-mixing-strategies.md) (no pure equilibrium), [references/axelrod-tit-for-tat-repeated-games.md](references/axelrod-tit-for-tat-repeated-games.md) (the repeated dilemma).
