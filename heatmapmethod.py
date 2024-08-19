import cv2
import numpy as np
from picamera2 import Picamera2

def calculate_laplacian_variance(image):
    # Apply Laplacian operator in the datatype of int16 to avoid overflow
    laplacian = cv2.Laplacian(image, cv2.CV_16S, ksize=3)
    laplacian = np.float32(laplacian)  # Convert to float for variance computation
    
    # Compute variance of Laplacian
    variance = cv2.blur(np.square(laplacian), (10, 10))  # Square of Laplacian values to find variance
    variance = variance / 100  # Normalize values for better visualization
    
    # Convert variance to heatmap
    heatmap = cv2.applyColorMap(np.uint8(variance), cv2.COLORMAP_JET)
    return heatmap

# Initialize Picamera2
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration()
picam2.configure(preview_config)
picam2.start()

# Prepare windows for displaying the frames and heatmap
cv2.namedWindow("Live Camera Feed", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Laplacian Variance Heatmap", cv2.WINDOW_AUTOSIZE)

try:
    while True:
        frame = picam2.capture_array()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

        # Display the live camera feed
        cv2.imshow("Live Camera Feed", frame)

        # Calculate and display the heatmap of Laplacian variance
        heatmap = calculate_laplacian_variance(frame)
        cv2.imshow("Laplacian Variance Heatmap", heatmap)

        # Exit loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
finally:
    picam2.stop()
    cv2.destroyAllWindows()
