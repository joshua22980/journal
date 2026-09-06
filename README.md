# Personal ADHD Assistant

This repository contains one **paste-ready source prompt** for a supportive daily
planning assistant: [`PROMPT.md`](PROMPT.md). It is deliberately short in its
day-to-day output, while the instructions behind that output include consent,
privacy, and failure handling.

## Set it up in ChatGPT

1. Create or edit a ChatGPT with custom instructions and paste in the complete
   contents of `PROMPT.md`.
2. Connect Gmail and Google Calendar only if those integrations are available to
   the account, and grant only the access the user is comfortable granting.
3. Set the user's IANA time zone (for example, `America/New_York`) in the prompt.
   Do not leave the placeholder in place.
4. Create these recurring scheduled tasks in ChatGPT (or in the user's calendar
   if scheduled tasks are unavailable):
   - **10:00 AM daily:** send `MORNING_START`
   - **12:30 PM daily:** send `CHECK_IN`
   - **2:30 PM daily:** send `CHECK_IN`
   - **4:35 PM daily:** send `CHECK_IN`
5. Test each trigger once. A written prompt cannot wake itself up, gain access to
   Google data, or prove that a reminder was created; the host product must
   provide and authorize those capabilities.

The 10:00 AM trigger is intentionally separate from the three check-ins. Times
are interpreted in the time zone configured in `PROMPT.md`.

## Why this is ADHD-informed

The design uses common cognitive-behavioral and environmental supports for adult
ADHD: externalizing plans, making tasks specific and manageable, reducing the
number of choices shown at once, using reminders, and responding to obstacles
with problem-solving rather than blame. It avoids presenting an arbitrary
15-minute timer as treatment: the prompt lets the user choose 15 or 30 minutes
and permits an even smaller starting action when stuck.

These choices are consistent with clinical guidance that emphasizes structure
in daily activities and may include ADHD-focused psychological interventions
with regular follow-up:

- [NICE guideline NG87: Attention deficit hyperactivity disorder](https://www.nice.org.uk/guidance/ng87/chapter/recommendations)
- [NICE quality standard QS39](https://www.nice.org.uk/guidance/qs39)
- [Cochrane review: Cognitive-behavioural interventions for ADHD in adults](https://www.cochrane.org/evidence/CD010840_cognitive-behavioural-interventions-attention-deficit-hyperactivity-disorder-adhd-adults)

This is a productivity accommodation, **not diagnosis, psychotherapy, or medical
care**. It should supplement—not replace—care from a qualified clinician. The
user remains in control and can pause check-ins or change the schedule at any
time.

## Design notes

- **Low-friction:** ordinary responses begin with one concrete action, not a long
  agenda.
- **No shame:** missed work is treated as information; the assistant helps shrink,
  clarify, switch, or defer the action.
- **Truthful tools:** Gmail, Calendar, and reminders are never claimed to have
  been checked or changed unless the relevant tool reports success.
- **Privacy-aware:** email and event contents are summarized only as needed and
  are not repeated unnecessarily.
- **Safety-aware:** urgent safety or health needs override the terse response
  format.

## Validate the source prompt

Run the repository's dependency-free validation before publishing changes:

```sh
python3 scripts/validate.py
```

The check verifies the exact schedule and check-in language, required safety and
tool-integrity text, and the structure and publishers of the evidence links. It
does not require internet access, so a restricted CI proxy cannot turn source
validation into a false failure.
