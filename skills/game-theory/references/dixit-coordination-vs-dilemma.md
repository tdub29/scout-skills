# Dixit & Nalebuff â€” Coordination Games vs. the Prisoner's Dilemma (and Changing the Game)

## The framework

> This game differs from the prisoners' dilemma of the previous chapter in many ways. Let us focus on one crucial difference. Fred's best choice depends on what Barney does, and vice versa. â€¦ unlike in the prisoners' dilemma, this game has no dominant strategies. (Chapter 4)

Not every game where players can "fail to cooperate" is a prisoners' dilemma. The strategic *structure* differs, and so does the fix. Diagnose which one you are in before prescribing a remedy.

### The three structures

- **Prisoners' dilemma.** Each player has a **dominant strategy to defect** (see `references/dixit-nash-equilibrium-dominance.md`); the unique equilibrium is mutual defection even though mutual cooperation is better for both. The problem is *incentive*: each is individually pulled to the bad outcome. Examples: price wars, the overfished commons, the studying "rat race."
- **Coordination / assurance game (the stag hunt).** Fred and Barney both do best by hunting the *same* big game, but neither has a dominant strategy â€” each one's best move depends on the other's. There are **two good Nash equilibria** (both-stag, both-bison) plus the safe-but-poor solo-rabbit option. The problem is not temptation but **uncertainty about what the other will do** and **which equilibrium to land on**. Cooperation is in everyone's interest *if they can be assured the others will cooperate too.*
- **Chicken.** Two equilibria, each asymmetric (you go straight while the rival swerves, or vice versa). Each player most wants to be the one who holds firm; the catastrophe is when both hold. The problem is a **contest over which equilibrium** is realized, with disaster if neither yields.

The dividing test: **is the bad outcome reached because defecting is each player's dominant strategy (dilemma), or because the players can't coordinate / can't trust which equilibrium will occur (coordination, assurance, chicken)?**

### Why the distinction changes the fix

- A **coordination/assurance** problem is solved by **information and salience** â€” a signal, a convention, a leader, a focal point that aligns expectations (see `references/schelling-focal-points.md`). Once each is assured the other will go for stag, both go for stag; no one needs to be coerced.
- A **dilemma** is *not* solved by communication alone (the dominant strategy survives talk). It needs the game itself changed.

### Collective-action problems and changing the game

The dilemma scales to many players: each student studying harder imposes a cost on all the others ("akin to a factory's polluting"), each fisherman over-fishing depletes the common stock, each company advertising defensively because the others do. The result is a rat race no individual will unilaterally stop. Dixit & Nalebuff catalog the ways to *change the game* so cooperation becomes the equilibrium:

1. **Enforcement / an enforceable collective agreement (a cartel).** The Ivy League schools jointly capped spring football training; OPEC limits output. The trouble is *detection and enforcement* â€” a "no-studying cartel" fails because secret studiers can't be caught (small towns enforce it socially by cruising Main Street to notice who's home studying).
2. **Outside enforcement.** Better still if an outsider imposes the restraint: the 1968 TV cigarette-advertising ban, which the companies fought but which ended up sparing them all the costly defensive advertising and raising every firm's profit.
3. **Repetition.** Ongoing interaction lets cooperation be sustained by the threat of future retaliation â€” the bridge to repeated games (see `references/axelrod-tit-for-tat-repeated-games.md`).
4. **Changing payoffs / penalties / property rights** so defection no longer dominates (taxes on the externality, quotas, fees for the common resource).

## How to apply

1. **Frame the game** â€” players, moves, payoffs (see the Nash/dominance reference). Check for dominant strategies.
2. **Classify the structure.** Dominant strategy to defect â†’ **prisoners' dilemma**. No dominant strategy, multiple good equilibria, players want to match â†’ **coordination/assurance**. No dominant strategy, asymmetric equilibria, players want to *differ* with disaster if both hold â†’ **chicken**.
3. **Match the remedy to the structure.** Coordination/assurance â†’ align expectations (signal, convention, focal point, leader). Dilemma/collective action â†’ change the game (enforceable agreement, outside enforcement, repetition, altered payoffs).
4. **For a cartel/agreement, design the enforcement.** Can defection be *detected*? Who has incentive to *punish* it? Without both, the agreement unravels.
5. **Prefer repetition and changed payoffs** for durable cooperation â€” they make cooperating each player's own best response rather than a coerced exception.

## Common failure modes

- **Misdiagnosing the structure.** Treating a coordination problem (just needs a shared signal) as a dilemma (and reaching for coercion), or vice versa.
- **"Just talk it out" applied to a true dilemma.** Communication doesn't dissolve a dominant strategy; the bad equilibrium returns the moment talk ends.
- **Cartel without enforcement.** Agreements to restrain competition collapse when cheating can't be detected or punished (the students' no-studying pact).
- **Ignoring the externality.** In collective-action problems the harm one player does the rest is unpriced; without making the actor bear it, exhortation fails.
- **Forgetting repetition can flip the result.** A one-shot dilemma may become solvable simply because the same players keep meeting.

## Manipulation-literacy note

"Changing the game" is powerful and can be turned against the public as easily as for it: a **cartel** is mutual cooperation among insiders that is *bad for everyone outside it* (the cigarette firms' collusion; price-fixing). Apply the discrimination note when an offensive use appears â€” **name the move** (is this a value-creating coordination or a collusion that extracts from outsiders?), **model the payoffs including third parties**, **flag** whether the "cooperation" benefits or harms those not at the table, and **prefer** arrangements whose enforcement is transparent and whose gains are not someone else's involuntary loss. The same theory runs in reverse: to *break* a harmful cartel, attack its detection-and-enforcement mechanism.

## References

- Avinash Dixit & Barry Nalebuff, *The Art of Strategy* (W. W. Norton, 2008), Chapter 4, "A Beautiful Equilibrium" (the stag/bison coordination game; chicken; multiple equilibria), and Chapter 9, "Cooperation and Coordination" (the studying rat race; Ivy League training cap; cartels; the 1968 cigarette-ad ban; outside enforcement).
- Related: [references/dixit-nash-equilibrium-dominance.md](references/dixit-nash-equilibrium-dominance.md) (dominance vs. multiple equilibria), [references/schelling-focal-points.md](references/schelling-focal-points.md) (how players pick one equilibrium without communicating), [references/axelrod-tit-for-tat-repeated-games.md](references/axelrod-tit-for-tat-repeated-games.md) (repetition as the cooperation engine), [references/dixit-credible-commitment.md](references/dixit-credible-commitment.md) (commitment as a way to change a chicken game).
