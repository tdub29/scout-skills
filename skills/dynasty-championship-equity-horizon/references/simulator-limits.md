# Step 10: Where the Simulator Stops Being Trustworthy

## Step 10: know where this simulator stops being trustworthy

Two measured artifacts. Both bite the out-years, which is exactly where a long horizon
puts its weight, so state them whenever you quote a season past +3.

**1. No roster persistence.** Each simulated season takes TODAY's roster, ages it, and
converts picks. It does not carry forward what would actually have happened: players
acquired, dropped, drafted, streamed, or aged out in the intervening simulated seasons.
A "+6 years" roster is "today's roster, six years older, every pick converted", not a
roster anyone would really be fielding. This biases **against** the strategy that
depends most on mid-course roster churn, which is a rebuild, because a real rebuilder
keeps trading through the sell phase and this model freezes him after one transaction.

**2. The draft-slot feedback loop oscillates.** `pickValueBySlot` rewards a bad finish
with a better pick, which is correct and necessary (without it losing buys nothing and
the model can only ever say contend). But because the roster does not persist, the loop
has no damping: a bad year earns a great pick, the pick converts, the roster jumps, the
next pick is bad, it falls back. Measured on one roster, do-nothing:

| | 2028 | 2029 | 2030 | 2031 | 2032 | 2033 |
|---|---|---|---|---|---|---|
| Feedback ON | 7.7% (#5) | 8.5% (#3) | 6.5% (#5) | 12.2% (#3) | 9.0% (#6) | 12.6% (#4) |
| Feedback OFF | 6.4% (#6) | 9.5% (#3) | 8.5% (#3) | 11.0% (#3) | 12.3% (#3) | 14.5% (#2) |

Feedback OFF is smooth and monotone. Feedback ON saws between 3rd and 6th. The
oscillation is an artifact, not a forecast.

**Rules that follow:**

- **Never quote a single out-year title percentage as a prediction.** Quote the trend.
- Read year-by-year figures only through +3. Past that, use the DIRECTION and the
  discounted total.
- Report both feedback settings when a verdict hinges on a season past +4. If the two
  disagree about the ranking of two strategies, the horizon cannot settle it and you
  should say so rather than pick.
- The long-horizon defence of a rebuild is legitimate, but it cannot rest on a single
  spiky out-year. A rebuild that wins only in 2032 and only with feedback ON has not
  been shown to win.
