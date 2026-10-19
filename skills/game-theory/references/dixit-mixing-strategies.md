# Dixit & Nalebuff â€” Mixing Strategies (Randomizing to Stay Unpredictable)

## The framework

> If you follow any system or pattern in your choices, it will be exploited by the other player to his advantage and to your disadvantage; therefore you should not follow any such system or pattern. (Chapter 5)

In some games there is **no equilibrium in pure (definite) strategies** â€” any fixed choice can be anticipated and beaten. The cure is a **mixed strategy**: choosing your action at random, according to fixed *probabilities*, so the other player cannot predict any single play. Dixit & Nalebuff open with Vizzini's poisoned-goblet "battle of wits" in *The Princess Bride*, where every line of reasoning is self-contradictory ("you would have counted on it, so I can clearly not choose the wine in front of meâ€¦ butâ€¦"). The circle has no logical end. The only valid conclusion is: **don't be predictable.**

### The canonical case: the penalty kick

A well-struck penalty reaches the goal in two-tenths of a second; the goalie must commit left or right *before* seeing the ball, and the kicker must choose before seeing the goalie lean. It is effectively a simultaneous, near-zero-sum game with no pure-strategy Nash equilibrium (see `references/dixit-nash-equilibrium-dominance.md`). A kicker known to favor one side gets that side covered and more kicks saved. The solution is to kick left a certain *fraction* of the time and right the rest, with the proportions chosen so the opponent cannot exploit you.

### How the best mix is computed (the equalizing principle)

Your best mix is the one that makes the opponent **indifferent** among his responses â€” it equalizes his payoff to whatever he does, so he gains nothing by leaning one way. Symmetrically, when *he* uses *his* best mix, *your* success rate is the same no matter which action you pick. That produces a tempting but wrong shortcut: "since I score 79.6% whatever I do against his best mix, I'll just always kick left." The flaw: **the reason to use your own best mix is to keep the other player using his.** If you settle on left, he stops mixing and covers left, and your payoff collapses. You randomize not to improve your score *against his current mix* but to deny him a profitable deviation.

### Where mixing applies

- **Repeated competitive plays:** tennis serves (down the T vs. wide), baseball pitch selection, football play-calling (the run up the middle stays a good "percentage play" *because* you throw the occasional bomb to keep the defense honest), poker (you must bluff with some frequency so your bets aren't readable).
- **One-shot plays with espionage risk:** in a battle, the point of attack is a unique decision, but if the enemy can spy out a *definite* plan he adapts to your maximum disadvantage. "You want to surprise the enemy; the surest way to do so is to surprise yourself" â€” keep options open and pick at the last moment with an espionage-proof random device whose proportions, even if discovered, can't be exploited.
- **Inspection / enforcement (an application of the same logic):** a tax authority, auditor, drug tester, or ticket inspector who checks on a *predictable* schedule invites evasion in the gaps; randomizing *which* and *when* to inspect (at a rate that makes cheating unprofitable in expectation) deters without inspecting everyone. The structure mirrors the penalty kick: the enforcer mixes to keep the evader honest.

## How to apply

1. **Diagnose the need to mix.** Is this a near-zero-sum, simultaneous game where any fixed choice can be read and countered? If so, no pure strategy is safe â€” mix.
2. **List your actions and the opponent's** and the payoffs (a 2x2 is the clean starting case).
3. **Find the mix that makes the opponent indifferent.** Choose your probabilities so the opponent's expected payoff is equal across his responses â€” then he can't exploit a lean. (For 2x2, this is a short algebra step; the principle generalizes.)
4. **Randomize for real.** Use an actual random device, not "feel." Humans alternate too much and clump too little, producing detectable patterns.
5. **Hold the mix to keep the opponent honest**, and pre-justify it: explain *before* the costly draw that mixing is what keeps your main play strong, because after a bad outcome the second-guessing is brutal.

## Common failure modes

- **Free-riding on the opponent's mix.** "I score the same whatever I do, so I'll just pick one." This invites him to stop mixing and counter you. Keep mixing to keep him mixing.
- **Fake randomness.** People asked to act randomly over-alternate (avoiding repeats) and so become predictable; only a genuine randomizer is espionage-proof.
- **Mixing a non-conflict game blindly.** In games with common interest as well as conflict (stag/bison), mixing has a role but with qualifications â€” it can leave value on the table versus coordinating. Don't randomize away a coordination win (see `references/schelling-focal-points.md`).
- **Outcome-judging a sound mix.** A correct mix still loses sometimes (the goalie occasionally guesses right; the bomb is intercepted). Judge the *strategy*, not the single result.
- **Over-elaborating.** Championship Rock-Paper-Scissors players who try to out-read opponents rather than randomize show no persistent advantage â€” cleverness about patterns rarely beats genuine unpredictability.

## References

- Avinash Dixit & Barry Nalebuff, *The Art of Strategy* (W. W. Norton, 2008), Chapter 5, "Choice and Chance" (the Vizzini battle of wits; soccer penalty kicks; the best mix and the equalizing logic; battle / espionage; the football "percentage play").
- Related: [references/dixit-nash-equilibrium-dominance.md](references/dixit-nash-equilibrium-dominance.md) (mixing solves games with no pure equilibrium), [references/dixit-backward-reasoning-game-trees.md](references/dixit-backward-reasoning-game-trees.md) (when *not* to reveal a move by going first).
