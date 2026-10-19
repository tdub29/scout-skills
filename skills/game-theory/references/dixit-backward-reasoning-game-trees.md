# Dixit & Nalebuff â€” Backward Reasoning on Game Trees

## The framework

> RULE 1: Look forward and reason backward. Anticipate where your initial decisions will ultimately lead and use this information to calculate your best choice. (Chapter 2)

A *sequential* game is one where players move in turn and each can see (or infer) the moves made before. The defining feature is **interdependence over time**: when it is your turn, your current action shapes the future actions of the others, and their future actions shape what you should do now. The first rule of strategy for these games is to look forward to the end of the game and reason backward to the present.

Dixit & Nalebuff open with Lucy holding the football for Charlie Brown. At the moment Charlie decides whether to run up and kick, Lucy's pull-away "lies in the future," but that does not make it *uncertain*: of the two outcomes Lucy can produce, she prefers seeing Charlie fall. So Charlie should forecast that she will pull the ball away and decline to play. Treating her future choice as a coin-flip is, in their phrase, "a triumph of hope over experience."

### Two kinds of strategic interaction

The chapter draws the master distinction the whole book runs on:

- **Sequential** â€” players alternate moves (Charlie/Lucy, chess). Each mover must look ahead to others' future responses *and* his own later choices. Solved by backward reasoning (this reference).
- **Simultaneous** â€” players act at the same time, each ignorant of the others' current move but aware that the others are reasoning too (the prisoner's dilemma). Solved by best-response / equilibrium analysis (see `references/dixit-nash-equilibrium-dominance.md`).

When you find yourself in a game, first **determine which kind it is**. Some games (football) have both elements; fit the method to the part.

### Decision trees and game trees

A *decision tree* maps one decider's options at each junction (Frost's two roads; the Princeton-to-New-York commute: bus/train/car, then which bridge or tunnel, then subway/bus/taxi). The right way to read it is **not** to take the branch that looks best at the first node and "cross the Verrazano when you get to it," but to anticipate the downstream choices and use them to pick the early branch â€” if you want to go downtown, the PATH train beats driving because of the connection at Newark.

A *game tree* is the same picture with one new element: **at different nodes it is different players' turn to move.** A player choosing early must forecast not only his own later choices but the others', by figuratively standing in their shoes at each future node, working out their best response there, and folding that answer back up the tree to the present.

### The backward-reasoning procedure

1. Draw the tree: nodes are decision points (labeled with whose turn it is), branches are the available actions, terminal nodes carry each player's payoff.
2. Start at the **last** decision nodes. At each, the player chooses the branch with the highest payoff *for that player*. Prune the others.
3. Replace each last node with the payoff that results from its best branch.
4. Step back one level and repeat â€” each earlier player now chooses knowing how the later player will respond.
5. The path of branches that survives all the way back to the root is the predicted play and the **first-mover's best move**.

### First-mover advantage (and its limits)

Moving first can be an advantage precisely because it *commits* you and forces the later mover to respond to a done deal â€” this is the bridge to commitment (see `references/dixit-credible-commitment.md`). But the advantage is not automatic. Moving first reveals information; in games where being predictable is fatal it is a *disadvantage* (see `references/dixit-mixing-strategies.md`). The tree tells you which case you are in.

## How to apply

1. **Confirm the game is sequential.** Do players observe earlier moves before responding? If they move blind and at once, you are in a simultaneous game â€” use the Nash/dominance reference instead.
2. **List the players in move order** and draw the tree. Keep it small first; the logic is clearest on a two- or three-move stub.
3. **Put real payoffs at the leaves** â€” even rough rankings (best/second/worst). Backward reasoning is only as good as the payoffs you assign to the *other* player, so put yourself in their shoes honestly, not hopefully.
4. **Prune from the end.** At each final node pick the mover's best branch; fold its payoff up; repeat to the root.
5. **Read off the prediction** â€” the surviving path â€” and ask the strategic question: can I improve my outcome by *changing the tree* (committing, adding a move, removing one of my own options) rather than just playing it well? That is the handoff to strategic moves.

## Common failure modes

- **Hope over experience.** Treating a rival's future choice as uncertain when their incentives make it predictable (Charlie Brown). Forecast what they *prefer*, not what you wish.
- **Reasoning forward / greedy-branch error.** Picking the branch that looks best at the first node without folding back the consequences ("cross the Verrazano when you get to it").
- **Mis-modeling the opponent's payoffs.** Backward induction is exact about the logic but garbage-in if you assume the other player wants what *you* would want.
- **Assuming unlimited look-ahead.** Real players have bounded foresight (chess engines prune; people satisfice). For prediction, model the depth the opponent can actually compute.
- **Confusing simultaneous with sequential.** If neither player observes the other before choosing, a tree gives a false sense of order.

## References

- Avinash Dixit & Barry Nalebuff, *The Art of Strategy* (W. W. Norton, 2008), Chapter 2, "Games Solvable by Backward Reasoning" (Rule 1; Charlie Brown; decision and game trees).
- Related: [references/dixit-nash-equilibrium-dominance.md](references/dixit-nash-equilibrium-dominance.md) (the simultaneous-move counterpart), [references/dixit-credible-commitment.md](references/dixit-credible-commitment.md) (turning a first move into a binding commitment), [references/dixit-mixing-strategies.md](references/dixit-mixing-strategies.md) (when moving first / being predictable backfires).
