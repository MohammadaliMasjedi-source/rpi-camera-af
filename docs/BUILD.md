# Build guide

A condensed index of the build. For the full walkthrough see
`Step by Step to implementation.pdf` and the photos in `Device setup/`.

## 1. Print the parts (`mountable items - 3D CAD/`)
- `Lens-Gear-modul-1.2-30T-30mm-outer-diam-extruded.stl` — gear attached to the lens focus ring
- `servo-gear-13T-thicker-longer.stl` — gear on the FS90R servo
- `Front-Cover-with-servo-mount.stl`, `front-frame.stl`, `back-frame.stl` — housing
- `pcb-mount.stl` — image-sensor / PCB mount

### Inspect the six meshes before printing

Run `python3 examples/inspect_parts.py` from the repository root. It reads only the STL files; no slicer, camera, third-party Python packages or GPIO are needed. You can also pass one or more binary STL paths to check replacement parts. Example results:

| Part | Triangles | Bounding-box span X × Y × Z (native units) |
|---|---:|---|
| Front frame | 1,368 | 89.00 × 60.00 × 16.00 |
| Back frame | 1,908 | 89.00 × 60.00 × 14.00 |
| Lens gear | 7,106 | 38.39 × 38.26 × 5.92 |

The front and back frames share a footprint but have different depths. Use the table to spot an accidental file swap before slicing. STL does not store units: compare a known physical dimension against the slicer preview before choosing a scale. Spans follow the file axes and do not establish fit, print orientation, tolerances or mesh watertightness.

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
The controller compares captured frames and pulses the servo. The lens position is not measured by an encoder; the score is not proof that a particular subject is in focus.

## Focus metrics
| Script | Method |
|--------|--------|
| `click_variance.py` | Reports grayscale Laplacian variance after masking a clicked region; no motor control |
| `heatmapmethod.py`  | Shows smoothed squared Laplacian response; no motor control |
| `Autofocus.py`      | Compares full-frame sharpness and drives the servo |
