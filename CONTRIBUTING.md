# Contributing

This is a completed seminar/project build (TU Clausthal, ETCE). It's shared as a reproducible
reference, but improvements are welcome.

## Ways to help
- **Built one yourself?** Open an issue with photos and any part/wiring tweaks you made.
- **Improved the focus algorithm?** PRs to `Autofocus.py` / the sharpness metrics are welcome.
- **Better CAD?** Drop revised STLs (and the source CAD if possible) in `mountable items - 3D CAD/`.

## Running the code (on the Pi)
```bash
python3 Autofocus.py
```
Requires a Raspberry Pi 4 with the camera enabled and the FS90R servo wired to the GPIO pin documented
in `Device setup/RPI used pins.jpg`.

## Conventions
- Keep the build **reproducible**: if you change hardware, update the photos and `docs/BUILD.md`.
- Keep curated sample images only; don't commit large capture dumps (see `.gitignore`).
