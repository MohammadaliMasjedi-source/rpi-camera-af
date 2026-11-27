<img src="https://www.presse.tu-clausthal.de/fileadmin/Presse/images/Corporate_Design/Logo/Logo_TUC_en_CMYK.jpg" width="300">

# RPI-Camera-AF
## Auto Focus Camera using Raspberry Pi, Lens, and a Servo Motor

[Photographed assembly](#component-installation-instructions) · [Printable parts and their dimensions](docs/BUILD.md#inspect-the-six-meshes-before-printing) · [Try a focus score on your laptop](#try-the-focus-idea-without-a-camera)

| Complete camera | Servo mount | Lens gear |
|:--|:--|:--|
| [![Assembled Raspberry Pi camera rig](Device%20setup/Complete%20device%20setup.jpg)](Device%20setup/Complete%20device%20setup.jpg) | [![Servo mounted on the front case](Device%20setup/Mount%20the%20Sevo-%20fs-90r%20to%20the%20front-case.jpg)](Device%20setup/Mount%20the%20Sevo-%20fs-90r%20to%20the%20front-case.jpg) | [![Ring gear fitted around the lens](Device%20setup/Month%20the%20ring%20gear%20on%20lens%2C%20using%20double%20side%20tape.jpg)](Device%20setup/Month%20the%20ring%20gear%20on%20lens%2C%20using%20double%20side%20tape.jpg) |

### Try the focus idea without a camera

Which looks sharper to a computer: one clean edge, or a row of alternating dark and light pixels? Run this from the repository root (Python 3, standard library only):

```sh
python3 examples/focus_scores.py
```

On the supplied synthetic rows, the scores are **0.00** (flat), **116.67** (soft edge), **3333.33** (sharp edge), and **40000.00** (alternating pattern). A high score means strong local changes; it does not establish that the lens is focused on your subject. Try doubling each value on the soft edge *without clipping*: what happens to the score?

[Explore the example](examples/focus_scores.py). It takes second differences along a single row at interior positions. The [actual camera code](Autofocus.py) uses the variance of a 2-D OpenCV Laplacian on grayscale frames. The demo neither drives a servo nor calibrates thresholds for the rig. New to Python? The [Persian Byte of Python project](https://github.com/MohammadaliMasjedi-source/a-byte-of-python-fa) introduces the lists and loops used here.

## The build and the control loop

This TU Clausthal ETCE seminar prototype uses a Raspberry Pi 4, a CSI camera with a manually focusable lens, and an FS90R continuous-rotation servo. Two printed gears couple the servo to the lens ring. The [original build report](Step%20by%20Step%20to%20implementation.pdf) and assembly photos document the working rig.

Picamera2 supplies frames, OpenCV measures sharpness and RPi.GPIO pulses the motor. The controller moves the lens a short step and compares the new frame's score with the preceding score. It changes direction when the score falls. After more than five reversals, it takes a photo and waits while the score stays within 10% of the frame score measured immediately before capture. The mechanism does not measure the lens angle or return to an independently measured best position.

The team's prototype responded to changes in the scene; the lens, servo and mechanical step size limited fine adjustment. A high score can come from texture in the background. Use the photographed build as a starting point, and evaluate focus on the intended subject before relying on it.

## What the three scripts actually do

- [Autofocus.py](Autofocus.py) compares frame scores and drives the servo. It is the hardware control program.
- [click_variance.py](click_variance.py) prints a score when you click. It zeros pixels outside a 50-pixel-radius circle, computes a grayscale Laplacian and takes the variance over the resulting image. The mask edge can affect that score. This viewer does not drive the motor.
- [heatmapmethod.py](heatmapmethod.py) displays spatially smoothed squared Laplacian response as a color heatmap alongside the feed. Strong edges or texture can stand out; it does not track motion or move the lens.

[Complete device setup](Device%20setup/Complete%20device%20setup.jpg)

[Step by step implementation guide to get the result](Step%20by%20Step%20to%20implementation.pdf)

[Python script](Autofocus.py)

[mountable items - 3D CAD](mountable%20items%20-%203D%20CAD)
## Assembly Instructions

Before you start the assembly, ensure you have all the necessary tools and components listed.

### Tools Required for Assembly:
Before beginning, gather the following tools:
1. iFixit Micro Screwdriver
2. Pliers
3. Wire Cutter/Stripper
4. Double-Sided Tape

### Hardware Components:
1. **Raspberry Pi 4**: Serves as the main controller of the camera.
2. **Micro SD Card (32 GB)**: For Raspberry Pi OS and software.
3. **3D-Printed Parts**: Listed below with corresponding CAD files.
   - [Front Frame](mountable%20items%20-%203D%20CAD/front-frame.stl)
   - [Front Cover](mountable%20items%20-%203D%20CAD/Front-Cover-with-servo-mount.stl)
   - [Back Frame](mountable%20items%20-%203D%20CAD/back-frame.stl)
   - [PCB Mount](mountable%20items%20-%203D%20CAD/pcb-mount.stl)
   - [Servo Gear Module](mountable%20items%20-%203D%20CAD/servo-gear-13T-thicker-longer.stl)
   - [Lens Gear Module](mountable%20items%20-%203D%20CAD/Lens-Gear-modul-1.2-30T-30mm-outer-diam-extruded.stl)
5. **Jumper Cables**: Male to Male and Male to Female.
6. **Camera Module**: HQ camera v1.0 and Arducam lenses 120 degree with manual focus.
7. **Power Supply**: 5V, 2.5-3A for Raspberry Pi.
8. **Micro HDMI Cable**
9. **Servo Motor**: Feetech FS90R 360° Continuous Rotation.

### Component Installation Instructions:
1. Mount the image sensor on the PCB Mount. [Image](Device%20setup/Mount%20the%20image%20censor%20on%20the%20PCB-Mount.jpg) | [CAD file](mountable%20items%20-%203D%20CAD/pcb-mount.stl)
2. Mount the ring gear on the lens using double-sided tape. [Image](Device%20setup/Month%20the%20ring%20gear%20on%20lens%2C%20using%20double%20side%20tape.jpg) | [CAD file](mountable%20items%20-%203D%20CAD/Lens-Gear-modul-1.2-30T-30mm-outer-diam-extruded.stl)
3. Attach the PCB mount to the Raspberry mount. [Image](Device%20setup/attach%20the%20PCB-mount%20to%20the%20Raspberry-mount.jpg) | [CAD file](mountable%20items%20-%203D%20CAD/back-frame.stl)
4. Mount the Raspberry on the Raspberry mount. [Image](Device%20setup/Mount%20the%20raspberry%20on%20the%20Raspberry-mount.jpg)
5. Connect the camera to the Camera connector on the board. [Image](Device%20setup/Connect%20the%20camera%20to%20the%20Camera-connector%20on%20the%20board.jpg)
6. Mount the lens on the camera. [Image](Device%20setup/Mount%20the%20lens%20on%20the%20camera.jpg)
7. Add the case extension to the Raspberry mount. [Image](Device%20setup/Add%20the%20case%20extention%20to%20on%20the%20Raspbery%20mount.jpg) | [CAD file](mountable%20items%20-%203D%20CAD/front-frame.stl)
8. Mount the Servo FS-90R to the front case. [Image](Device%20setup/Mount%20the%20Sevo-%20fs-90r%20to%20the%20front-case.jpg) | [CAD file](mountable%20items%20-%203D%20CAD/Front-Cover-with-servo-mount.stl)
9. Connect the jumper wire to the desired GPIO pins. [Image](Device%20setup/Connect%20the%20jumper%20wire%20to%20the%20desire%20GPIO%20pins.jpg)
10. Mount the Motor gear. [Image](Device%20setup/Mount%20the%20Motor%20gear.jpg) | [CAD file](mountable%20items%20-%203D%20CAD/servo-gear-13T-thicker-longer.stl)
11. Fix the front case lid, and secure with Cable tie-wraps. [Image](Device%20setup/Fix%20the%20front%20case%20lid%2C%20and%20tie%20with%20Cable%20tie-wrap.jpg)
