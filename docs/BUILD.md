# Build guide

A condensed index of the build. For the full walkthrough see
`Step by Step to implementation.pdf` and the photos in `Device setup/`.

## 1. Print the parts (`mountable items - 3D CAD/`)
- `Lens-Gear-modul-1.2-30T-30mm-outer-diam-extruded.stl` — gear that clamps to the lens focus ring
- `servo-gear-13T-thicker-longer.stl` — gear on the FS90R servo
- `Front-Cover-with-servo-mount.stl`, `front-frame.stl`, `back-frame.stl` — housing
- `pcb-mount.stl` — image-sensor / PCB mount

## 2. Assemble
1. Mount the lens on the camera; mount the image sensor on the PCB mount.
2. Attach the PCB mount to the Raspberry Pi mount.
3. Mount the FS90R servo to the front case; fit the servo gear.
4. Mount the lens-ring gear with double-sided tape so it meshes with the servo gear.
5. Mount the Raspberry Pi; close and cable-tie the front case.

*(Each step has a photo in `Device setup/`.)*

## 3. Wire it
Connect the FS90R servo signal to the GPIO pin shown in `Device setup/RPI used pins.jpg`
(power and ground to the Pi's 5V/GND rails).

## 4. Run autofocus
```bash
python3 Autofocus.py
```
The script sweeps the servo across the focus range, scores each frame's sharpness, and parks at the
sharpest position.

## Focus metrics
| Script | Method |
|--------|--------|
| `click_variance.py` | Pixel-intensity **variance** as the sharpness score |
| `heatmapmethod.py`  | **Heatmap** based sharpness evaluation |
| `Autofocus.py`      | Drives the servo sweep and selects peak focus |
