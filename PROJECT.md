# 📷 RPi Camera Autofocus
> Camera autofocus on Raspberry Pi 4 driving an FS90R servo - Python focus algorithms, 3D-printed mounts, and a step-by-step build guide.

**Status:** shipped · **Priority:** low · **Progress:** 100% · **Private:** no
**Links:** [GitHub](https://github.com/MohammadaliMasjedi-source/rpi-camera-af) · [Dashboard](dashboard/index.html)

> Seminar / project work in the ETCE department of TU Clausthal. Companion to `.mc/project.json`.

## Vision
A complete, reproducible **autofocus rig**: a Raspberry Pi 4 turns a lens focus ring through a 3D-printed
gear driven by an FS90R servo, while a Python sharpness metric finds the in-focus position. Everything
needed to rebuild it - code, 3D-printable parts, wiring, and a photo build guide - lives in this repo.

## Phases
### Phase 1 — Mechanics + electronics  ✅ 100%
- [x] 3D-printed lens gear, servo mount, frames (`mountable items - 3D CAD/`)
- [x] Wire FS90R servo to RPi4 GPIO
- [x] Mount camera + image sensor

### Phase 2 — Focus algorithm  ✅ 100%
- [x] Sharpness metric — variance (`click_variance.py`) / heatmap (`heatmapmethod.py`)
- [x] Servo sweep + peak-focus search (`Autofocus.py`)

### Phase 3 — Documentation  ✅ 100%
- [x] Step-by-step build guide (`Step by Step to implementation.pdf` + `Device setup/` photos)
- [x] README + `Script description.txt`

## Approach
`Autofocus.py` sweeps the FS90R servo across the focus range and scores each frame's sharpness; the
position with the highest score is selected. Two sharpness metrics are provided: a pixel-variance
method and a heatmap method. Mechanical parts are parametric STLs printable on a standard FDM printer.

## Hardware
- Raspberry Pi 4 + Pi camera
- FS90R continuous-rotation micro servo
- 3D-printed: lens gear (module 1.2, 30T), servo gear (13T), front cover with servo mount, frames, PCB mount

## Decisions (log)
| Date | Decision | Why | Rejected |
|------|----------|-----|----------|
| 2024-09-09 | Variance/heatmap sharpness metric | Simple, fast, robust on-device | FFT-based sharpness |

## SWOT
- **Strengths** — complete reproducible build; documented end to end; low-cost parts.
- **Weaknesses** — FS90R is continuous-rotation (open-loop positioning); single lens tested.
- **Opportunities** — closed-loop with an encoder; reuse the focus metric on other rigs.
- **Threats** — tied to a specific RPi camera stack.

## Build it
See `docs/BUILD.md`, the photos in `Device setup/`, and `Step by Step to implementation.pdf`.

## ✅ Definition of Done (certified 2026-07-14)
**DONE** — a *documented, working hardware prototype*. "Done" here means the rig can be rebuilt
from this repo alone:
- **Autofocus code present + syntax-valid** — `Autofocus.py` uses Laplacian-variance sharpness
  (`is_blurred()` → `cv2.Laplacian(...).var()`), FS90R servo control (`rightmove()` / `leftmove()`
  via PWM duty cycle), and a threaded live-preview + peak-focus sweep. Plus `click_variance.py`
  (variance) and `heatmapmethod.py` (heatmap) focus metrics. All three parse clean.
- **Hardware fully documented** — all 7 CAD STLs in `mountable items - 3D CAD/`, every wiring/
  assembly photo in `Device setup/`, and `docs/BUILD.md` + `Step by Step to implementation.pdf`
  cover print → assemble → wire → run end to end.
- **Limitations noted honestly** — FS90R is continuous-rotation ⇒ open-loop, no micro-adjustment;
  single lens/camera tested; tied to the RPi PiCamera2 stack; the script needs real RPi4 + camera
  + servo hardware to execute.

*Note:* the README hyperlinks point at the upstream `ETCE-LAB` repo, but every file they reference
also lives here, so this repo is self-contained and reproducible.
