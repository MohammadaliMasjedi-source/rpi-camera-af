import cv2
import numpy as np
from picamera2 import Picamera2, Preview

def calculate_laplacian_variance(image, center, radius):
    # Create a mask with the same dimensions as the image, with a filled circle at the click location
    mask = np.zeros_like(image, dtype=np.uint8)
    cv2.circle(mask, center, radius, (255, 255, 255), thickness=-1)

    # Apply the mask to the image
    masked_image = cv2.bitwise_and(image, mask)

    # Convert masked image to grayscale
    gray_image = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

    # Calculate the Laplacian
    laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
    variance = laplacian.var()

    return variance

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Calculate the Laplacian variance for the circle with the center at (x, y) and radius 50
        frame = param['frame']
        variance = calculate_laplacian_variance(frame, (x, y), 50)
        print(f'Laplacian Variance at ({x}, {y}): {variance}')

def main():
    # Initialize the camera
    picam2 = Picamera2()

    # Configure the camera with 600x600 resolution
    camera_config = picam2.create_preview_configuration(main={"size": (600, 600)})
    picam2.configure(camera_config)

    # Start the camera
    picam2.start()

    try:
        cv2.namedWindow('Live View')
        frame = None

        while True:
            # Capture frame-by-frame
            frame = picam2.capture_array()

            # Convert to RGB color
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Display the resulting frame
            cv2.imshow('Live View', rgb_frame)

            # Set mouse callback function with the current frame
            cv2.setMouseCallback('Live View', mouse_callback, param={'frame': rgb_frame})

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # When everything done, release the capture
        picam2.stop()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
