# AGENTS.md — RPi Camera Autofocus

Read this first if you are an AI coding agent (Claude Code, OpenAI Codex, or any other) or a
human landing on this repo.

## What this project is
A modular Raspberry Pi 4 camera rig with servo-driven autofocus: a Laplacian-variance sharpness
metric (`Autofocus.py`, `click_variance.py`, `heatmapmethod.py`) drives an FS90R servo through
3D-printed gears to hunt for peak focus. Fully documented build (CAD STLs, wiring photos,
step-by-step PDF).

## Classification
**PUBLIC — open license (GPL-3.0), `private: false` in `.mc/project.json`. External human
contributors welcome via a normal PR, still subject to the AI-verification rule below.**

## Where the real state lives
1. `.mc/project.json` — canon: `status: "shipped"`, `progress: 100`, and the `dod` block that
   already records what "certified done" means for this build.
2. `README.md` — the full build/assembly/wiring guide (this repo doubles as its own docs).
3. `Step by Step to implementation.pdf` + `Device setup/` — the photographed build steps.

## Definition of Done
- [ ] Any code change to `Autofocus.py` / `click_variance.py` / `heatmapmethod.py` stays
  syntax-valid Python and keeps `is_blurred()`, `rightmove()`/`leftmove()` working the same way
  documented in the README — this is a hardware-in-the-loop project, so a full test means running
  it on the real RPi4 + camera + servo rig, not just an import check.
- [ ] If you touch the CAD files (`mountable items - 3D CAD/`) or the wiring instructions, update
  the corresponding photo/step in `Device setup/` and the README table so the two never diverge.
- [ ] AI-drafted changes get a second, independent pass before being trusted (Iron Rule 1,
  `Pantheon/docs/ROUTING-POLICY.md`) — doubly true here since this is `PUBLIC` and external PRs
  may land too.
- [ ] No secrets committed (none expected in this repo — it's hardware + docs).
- [ ] `.mc/project.json` `nextAction` updated only if real work resumes (currently
  "archive/maintenance only" — don't invent activity here without a reason).
- [ ] Real commit message; `git pull --rebase --autostash` before push; no `--no-verify`; no
  force-push to `main`.

## If blocked
This repo is stable/shipped — if you think something needs fixing, leave a note under
`## Blocked` in `.mc/INBOX.md` (create it if it doesn't exist) rather than reworking a documented,
working build on a guess.
