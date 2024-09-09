<img src="https://www.presse.tu-clausthal.de/fileadmin/Presse/images/Corporate_Design/Logo/Logo_TUC_en_CMYK.jpg" width="300">
# RPI-Camera-AF
## Auto Focus Camera using Raspberry Pi, Lens, and a Servo Motor

### Overview
The RPI-Camera-AF project leverages the versatile Raspberry Pi platform to create a modular camera system capable of automatic focusing. This innovative setup utilizes a combination of a high-quality lens, a precise servo motor, and custom 3D-printed components, orchestrated by the powerful Raspberry Pi 4 to enhance image clarity dynamically.

### Project Goal
The primary objective of this project is to develop a reliable autofocus mechanism that can adapt in real-time to different focusing needs. This system is designed to be especially beneficial in environments where focus accuracy is critical, such as in wildlife photography, surveillance, or any dynamic shooting scenario.

### Key Features
- **Dynamic Autofocus**: Utilizes advanced algorithms to adjust focus based on real-time image analysis.
- **Modular Design**: Components can be easily customized or replaced to suit different use cases or improve functionality.
- **Hands-On Learning**: Provides an educational platform for understanding and experimenting with image processing, hardware interaction, and software control.

Stay tuned for more updates as we continue to enhance system capabilities and explore new features!



## Abstract
This project aimed to design and develop a modular camera platform using a Raspberry Pi, integrating various components such as a camera sensor, a wide lens, an FS90R servo motor, and 3D-printed gears. The primary objective was to create an autofocus mechanism that dynamically adjusts focus by calculating the Laplacian variance of live frame previews to achieve optimal sharpness. The methodology involved assembling the hardware components, programming the Raspberry Pi to control the servo motor based on image sharpness metrics, and enabling real-time focus adjustments. Initial tests demonstrated that while the system could effectively identify and adjust to changes in frame sharpness, limitations related to the precision of the lens's focal point, the quality of the sensor, and the accuracy of the servo motor control were identified. These factors affected the overall efficacy of the autofocus system. The project concluded that while the prototype showed potential, enhancements in hardware precision and control algorithms are necessary for practical applications. Future work will focus on refining these elements to improve system reliability and performance.

## Materials and Methods
In this project, we employed several hardware components and software tools to build our modular camera system. The core of our setup was the **Raspberry Pi 4**, a powerful model with sufficient processing capabilities for image handling and device control. This microcontroller was chosen for its robust support and the ability to interface with various peripherals via its GPIO (General Purpose Input/Output) pins.

### Hardware Components:
- **Raspberry Pi 4**: Serves as the processing unit and control hub.
- **Camera Sensor**: Connects to the Raspberry Pi via the 2-lane MIPI CSI camera port for capturing high-quality images.
- **FS90R Servo Motor**: Compact and lightweight, this motor adjusts the camera lens's focus, interfacing with the Raspberry Pi's GPIO pins.
- **3D-Printed Gears**: One gear mounted on the camera lens and the other on the servo motor to mesh perfectly and enable precise focus adjustments.

### Software Tools:
- **OpenCV (CV2)**: Used for real-time image processing, including calculating the Laplacian variance to determine image sharpness.
- **PiCamera 2 Library**: Designed for interfacing with the Raspberry Pi's camera module to capture and manipulate images directly.
- **RPi.GPIO Library**: Manages the GPIO pins for servo motor control, providing necessary instructions based on the image processing results.

### Assembly Process:
The assembly process involved carefully integrating these components. We started by connecting the camera sensor to the Raspberry Pi via the MIPI CSI port and setting up the servo motor via the GPIO pins. Next, the gears were attached—one on the lens and the other on the servo motor. We positioned the motor close enough to the lens so that the gears could engage correctly to transfer motion from the motor to the lens. This setup ensured that when the motor activated, the lens would rotate to adjust focus based on our software analysis. This methodical assembly ensured all parts worked in harmony, allowing for precise control and optimal image clarity.

## System Design and Implementation

Our modular camera system is designed to automate focusing through a manual lens using a Raspberry Pi 4 as the central controller. It features a well-coordinated assembly of hardware and software components.

### Hardware Components
- **Raspberry Pi 4**: Serves as the central processing unit, interfacing with the camera sensor via the 2-lane MIPI CSI camera port for high-quality image capture.
- **FS90R Servo Motor**: Manages autofocus by adjusting the lens position based on focus requirements, controlled through the Raspberry Pi’s GPIO pins.
- **3D-Printed Gears**: Engages between the lens and the servo motor, facilitating manual focus adjustments by translating motor movements into direct lens focus adjustments.

### Software Components
- **Python Libraries**:
  - **cv2**: Handles image processing tasks, such as calculating image sharpness.
  - **PiCamera 2**: Manages camera operations.
  - **RPi.GPIO**: Controls the GPIO pins that drive the servo motor.
  - **Threading Module**: Utilizes Python’s threading capabilities to maintain a live view from the camera while adjusting focus in real-time.

### System Operation
The system uses a Python script that integrates and controls these components effectively:
- **FrameVarianceMonitor Class**: Tracks the sharpness of consecutive images, storing variance values to determine when maximum focus is achieved.
- **Motor Control Functions (`rightmove()`, `leftmove()`)**: Adjust the motor’s direction and focus using `pwm.ChangeDutyCycle` to send signals to the servo.
- **Main Function (`moarso()`)**: Orchestrates the autofocus process by comparing sharpness values from consecutive frames and deciding the motor’s direction based on whether image sharpness is improving.

### Integration and Functionality
- **Servo Motor and Lens Integration**: The servo motor's integration with the lens via 3D-printed gears is a key aspect of our design, ensuring that each motor adjustment translates directly into lens movement.
- **Python Script Management**: Handles the complex task of focusing by continuously analyzing image quality and adjusting the lens position to ensure the camera system captures clear images and operates efficiently.
- **System Flexibility**: Designed to be robust yet adaptable, allowing for real-time adjustments and optimizations based on immediate feedback from the image processing algorithms.

### Advanced Focusing Methods
To enhance the focusing capabilities of our system, we have implemented various innovative methods, each tailored to optimize image clarity under different scenarios. These methods fully leverage the programmable features of the Raspberry Pi and our mechanical setup.

This comprehensive design and implementation ensure our camera system not only captures clear images but also maintains a balance between performance and simplicity in its operation.

## Advanced Focusing Techniques

To enhance the focusing capabilities of our camera system, we have implemented various innovative methods, each tailored to optimize image clarity under different scenarios. These methods fully leverage the programmable features of the Raspberry Pi and our mechanical setup.

### 1. Heatmap-Based Focusing
This method involves analyzing the 'heat' distribution in a frame to determine areas of highest activity or change, which often correspond to important focal points in an image. By generating a heatmap of each frame, the system identifies the 'hottest' part, which is likely to need sharper focus. This technique is particularly useful in dynamic environments, such as in wildlife photography or security applications.

### 2. Section-Based Focus
This user-driven method allows for selective focusing based on the user's input via a mouse click. When a section of the image is selected, the system focuses specifically on that area, adjusting the lens accordingly. This method is especially beneficial for controlled scenarios like macro photography or when precise depth of field control is desired. It provides the user with the flexibility to prioritize specific parts of the scene over others.

### 3. Comprehensive Frame Focusing
We explored two strategies to achieve optimal focus across the entire frame:
- **Threshold Strategy**: Sets a threshold for the number of attempts the system will make to find the frame with the highest variance—indicative of sharp focus—before stopping and capturing the image.
- **Rotational Strategy**: Involves rotating the lens in both directions multiple times to determine the optimum lens position, ensuring that the focus is refined by considering multiple positions and selecting the one that consistently provides the best clarity.

### Challenges and Refinements
One of the main challenges we encountered was the inability to achieve micro-adjustments with the motor and lens system, as the gears and motor setup did not allow for minute, millimeter-level changes. This limitation made it difficult to achieve extremely precise focus, particularly in scenarios requiring a very shallow depth of field or when dealing with micro-scale subjects. However, through iterative testing and refinement, we developed practical algorithms that approximate the best possible focus within the mechanical constraints. Once the optimal focus position is found, the system maintains that position until a significant change in the scene is detected—such as movements or lighting changes—which triggers a re-evaluation of the focus to ensure continuous clarity.

These methods collectively enhance the usability and functionality of our camera system, providing both automated and user-controllable options to achieve the desired focus, and adaptively responding to changes in the environment to maintain image quality.



[Complete device setup](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Complete%20device%20setup.jpg)

[Step by step implementation guide to get the result](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Step%20by%20Step%20to%20implementation.pdf)

[Python script](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Autofocus.py)

[mountable items - 3D CAD](https://github.com/ETCE-LAB/rpi-camera-af/tree/main/mountable%20items%20-%203D%20CAD)
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
   - [Front Frame](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/back-frame.stl)
   - [Front Cover](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/Front-Cover-with-servo-mount.stl)
   - [Back Frame](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/back-frame.stl)
   - [PCB Mount](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/pcb-mount.stl)
   - [Servo Gear Module](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/servo-gear-13T-thicker-longer.stl)
   - [Lens Gear Module](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/Lens-Gear-modul-1.2-30T-30mm-outer-diam-extruded.stl)
5. **Jumper Cables**: Male to Male and Male to Female.
6. **Camera Module**: HQ camera v1.0 and Arducam lenses 120 degree with manual focus.
7. **Power Supply**: 5V, 2.5-3A for Raspberry Pi.
8. **Micro HDMI Cable**
9. **Servo Motor**: Feetech FS90R 360° Continuous Rotation.

### Component Installation Instructions:
1. Mount the image sensor on the PCB Mount. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Mount%20the%20image%20sensor%20on%20the%20PCB-Mount.jpg) | [CAD file](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/pcb-mount.stl)
2. Mount the ring gear on the lens using double-sided tape. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Mount%20the%20ring%20gear%20on%20lens%2C%20using%20double%20side%20tape.jpg) | [CAD file](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/Lens-Gear-modul-1.2-30T-30mm-outer-diam-extruded.stl)
3. Attach the PCB mount to the Raspberry mount. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/attach%20the%20PCB-mount%20to%20the%20Raspberry-mount.jpg) | [CAD file](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/back-frame.stl)
4. Mount the Raspberry on the Raspberry mount. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Mount%20the%20raspberry%20on%20the%20Raspberry-mount.jpg)
5. Connect the camera to the Camera connector on the board. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Connect%20the%20camera%20to%20the%20Camera-connector%20on%20the%20board.jpg)
6. Mount the lens on the camera. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Mount%20the%20lens%20on%20the%20camera.jpg)
7. Add the case extension to the Raspberry mount. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Add%20the%20case%20extension%20to%20on%20the%20Raspberry%20mount.jpg) | [CAD file](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/front-frame.stl)
8. Mount the Servo FS-90R to the front case. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Mount%20the%20Servo-%20fs-90r%20to%20the%20front-case.jpg) | [CAD file](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/Front-Cover-with-servo-mount.stl)
9. Connect the jumper wire to the desired GPIO pins. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Connect%20the%20jumper%20wire%20to%20the%20desire%20GPIO%20pins.jpg)
10. Mount the Motor gear. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Mount%20the%20Motor%20gear.jpg) | [CAD file](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/mountable%20items%20-%203D%20CAD/servo-gear-13T-thicker-longer.stl)
11. Fix the front case lid, and secure with Cable tie-wraps. [Image](https://github.com/ETCE-LAB/rpi-camera-af/blob/main/Device%20setup/Fix%20the%20front%20case%20lid%2C%20and%20tie%20with%20Cable%20tie-wrap.jpg)

This comprehensive guide will ensure a smooth assembly process for your modular camera system.
