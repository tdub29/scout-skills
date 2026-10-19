---
name: affirmation-studio
description: Turn a growth area, insecurity, or inner-child block into present-tense, believable, first-person affirmation and manifestation scripts formatted for recording in the user's OWN cloned voice with voicebox (local AI voice studio). Use when the user wants self-recorded affirmations, a manifestation or visualization script, a morning incantation, "I am" identity statements, a confidence/priming track, a self-talk rewrite, or to turn something from growth-areas.md into a daily audio practice. Triggers â€” affirmations, self-affirmation, affirmation script, manifestation, manifest, "I am" statements, incantations, morning routine audio, visualization script, priming, self-talk, "record affirmations in my voice," "clone my voice," voicebox, confidence script, hype track, law of attraction (reframed as intention/priming/visualization), growth-areas.md, "make me a track for X." Pairs with ning-li-inner-child-alchemy (reparenting / self-compassion framing for shame-heavy areas) and trevor-voice (so written lines sound like the user). GUARDRAILS: this is motivational self-reflection, priming, and visualization â€” NOT therapy, medical or mental-health treatment, or a guarantee of outcomes. Use the believability ladder (grandiose affirmations can backfire for people who don't yet believe them). Escalate active crisis, self-harm intent, or ongoing abuse to licensed care. Load references/ before generating.
---

# affirmation-studio

Generate affirmation and manifestation **scripts** that the user records in their **own cloned voice** with [voicebox](https://github.com/jamiepine/voicebox) (local-first AI voice studio: clone, dictate, create â€” MIT, runs entirely on-device). The script is the product; voicebox is the recording surface. Hearing your own voice say present-tense, believable identity statements is the point â€” so the default voice is the user's clone, first person.

This is a **priming and self-reflection** tool, not therapy and not magical thinking. Affirmations work by rehearsing identity, directing attention, and lowering the activation energy of a desired behavior â€” not by guaranteeing outcomes. Keep that honesty in the room and the practice stays credible.

## When to use

- The user names something from `self/growth-areas.md` (or any insecurity / goal) and wants a daily audio practice around it.
- The user asks for affirmations, an "I am" set, a manifestation/visualization script, a morning incantation, a hype/confidence track, or a self-talk rewrite.
- The user wants to record any of the above in their own voice via voicebox.

Do **not** use this for clinical distress â€” see Guardrails.

## Guardrails (read before generating)

- **Not therapy or treatment.** Output is journaling/priming/visualization text only. Don't diagnose, don't give medical or medication advice, don't promise cures or guaranteed results.
- **Hard stops â€” do not generate a track; point to licensed care + crisis resources:** active self-harm intent or plan, ongoing abuse or an unsafe living situation, severe dissociation, or a request to replace a therapist. (Same bar as `ning-li-inner-child-alchemy`.)
- **The believability problem is real.** Grandiose affirmations a person doesn't believe ("I am a millionaire," "I am fearless") can *lower* mood and self-esteem for those who need them most (Wood, Perunovic & Lee, 2009). Default to the **believability ladder** in `references/affirmation-craft.md` â€” claim only what the user can say without their gut calling it a lie, then ladder up.
- **Manifestation is framed as intention + attention + visualization**, never as a substitute for action or as a guarantee. If the user wants "law of attraction" language, translate it into priming/visualization the user can stand behind; flag if they want it kept literal.
- **One area per track.** Don't blend five growth areas into one diffuse script.

## Inputs to gather (ask only what's missing)

1. **Area / goal** â€” one growth area, insecurity, or concrete outcome.
2. **Believability check** â€” for a candidate line, "could you say this out loud right now without your gut calling it a lie?" Calibrates the ladder.
3. **Evidence** â€” 1â€“3 true past moments that prove the desired trait is *already* sometimes present (fuels the "because" lines and keeps it honest).
4. **Tone** â€” gentle/reparenting vs. firm/coach vs. hype. (Shame-heavy areas â†’ gentle; route to `ning-li-inner-child-alchemy` for the inner-child voice.)
5. **Length** â€” default ~60â€“120s read (8â€“14 lines). Morning loop vs. one-time.

If the user just says "make me a track for X," infer sensible defaults, generate, and tell them what to tweak.

## The method

Read `references/affirmation-craft.md` in full, then build the script in this shape (full template in `templates/affirmation-script.md`):

1. **Grounding line** â€” one breath / one intention. ("I'm here. One breath. This is mine to choose.")
2. **5â€“10 affirmations** â€” present tense, first person, positive framing (move-toward, never "I am not anxious"). Each sits on the believability ladder at a rung the user accepts:
   - Flat: `I am ___.`
   - Becoming: `I am becoming ___.` / `It's getting easier to ___.`
   - Choosing: `I am choosing to ___.` / `I am learning to ___.`
   - Capacity: `I am the kind of person who ___.`
3. **2â€“4 "because" lines** â€” reason-why evidence from the user's real past. ("Because I already did it when ___.") This is what makes the flat claims land.
4. **Short present-tense visualization** (2â€“5 sentences) â€” the desired scene as if now, sensory and specific. This is the "manifest" beat: see it, feel it, name the next concrete action it implies.
5. **Closing / reparenting line** â€” self-compassion. For shame-heavy areas, speak to the inner child (pull the voice from `ning-li-inner-child-alchemy`).

Then deliver the **voicebox recording steps** from `references/voicebox-recording.md`: record a clean voice sample â†’ create the clone â†’ paste the script â†’ generate â†’ save the audio â†’ loop it into the chosen routine.

## Output format

- The script as **clean spoken text** (no markdown headers inside the read, no stage directions in the spoken lines) â€” voicebox reads exactly what's pasted. Put any direction in a separate "notes" block.
- A one-line **believability note** flagging any rung you set and why.
- The **voicebox steps** (or a pointer to them if the user already has their clone set up).
- Offer to save the script to `self/affirmations/scripts/<area>.md` and to log the session.

## Failure modes

- **Grandiosity** â€” writing lines the user can't yet believe; ignoring the ladder.
- **Negation framing** â€” "I don't get anxious" instead of "I stay steady." The brain rehearses the noun.
- **Vague** â€” "I am successful" with no behavior, identity, or evidence attached.
- **No evidence** â€” affirmations with nothing true underneath them; they read as wishful and don't stick.
- **Therapy drift** â€” treating a clinical issue as an affirmation problem instead of escalating.
- **Tool-first** â€” leading with voicebox install instead of the script. Script first; the voice is the delivery.

## References

- [references/affirmation-craft.md](references/affirmation-craft.md) â€” the craft: believability ladder, present-tense/positive framing, specificity, evidence/reason-why, visualization, the self-affirmation research caveat, manifestation reframe.
- [references/voicebox-recording.md](references/voicebox-recording.md) â€” install voicebox, record a clean sample, clone your voice, generate the track, audio + loop tips.
- [templates/affirmation-script.md](templates/affirmation-script.md) â€” fill-in script skeleton.

Personal practice & where audio lives: `self/affirmations/` (see its README).
