import time
import cv2
from picamera2 import Picamera2
import RPi.GPIO as GPIO
import threading
import queue
import numpy
from collections import deque
from datetime import datetime

class FrameVarianceMonitor:
	# Initialize the monitor with a specific window size.
	def __init__(self, window_size):
		self.window_size = window_size			# Size of the sliding window for variance values
		self.variances = deque(maxlen=window_size)	# Fixed-size deque to store the latest variances
		self.current_max = float('-inf')		# Initialize the maximum variance found as negative infinity
	# Add a variance value to the deque and update the maximum variance if necessary.
   	def add_variance(self, variance):
		if variance>11:
			self.variances.append(variance)
		if len(self.variances) == self.window_size:	# When window is full
			self.current_max = max(self.variances)	# Update the maximum variance over the current window
		else:
			if variance > self.current_max:		# Check if the new variance is greater than the current max
				self.current_max = variance	# Update the maximum variance
	# Return the maximum variance found in the current window.
	def get_max_variance(self):
		return self.current_max
	# Check if the maximum variance value is in the current window and reset if true.
	def is_maximum_found(self):
		if len(self.variances) == self.window_size and self.current_max in self.variances:
			self.clear_variances()			# Reset the variances deque
			return True
		return False
	# Clear all stored variances and reset the maximum variance.
	def clear_variances(self):
		self.variances.clear()
		self.current_max = float('-inf')		# Reset the maximum variance to negative infinity

window_size = 30						# Set the window size for the variance monitor
monitor = FrameVarianceMonitor(window_size)			# Create an instance of FrameVarianceMonitor with the specified window size

servo_pin = 11 							# Define the GPIO pin number that will control the servo
GPIO.setmode(GPIO.BOARD)					# Set the GPIO pin numbering to 'BOARD' style
GPIO.setup(servo_pin, GPIO.OUT)					# Set up the servo pin as an output pin
pwm = GPIO.PWM(servo_pin, 50)					# Initialize PWM on the servo pin with a frequency of 50 Hz
pwm.start(0)							# Start PWM with 0% duty cycle (servo in neutral position)
picam2 = Picamera2()						# Initialize the camera object for the Raspberry Pi
video_config = picam2.create_video_configuration(main={"size": (480,360)})# Create a video configuration with a resolution of 480x360 pixels
size_tuple = video_config['main']['size']			# Extract the size from the video configuration to a tuple
size_str = str(size_tuple)					# Convert the size tuple to a string format
picam2.configure(video_config)					# Apply the video configuration to the camera
picam2.start()							# Start the camera to begin capturing video

# Calculate frame variance
def is_blurred(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)		# Convert the input image to grayscale for processing
	lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()  	# Apply the Laplacian operator to detect edges and calculate the variance of the result
	return int(lap_var)					# Return the variance as an integer, A lower variance indicates less edges, suggesting the image might be blurred

# set rotation to true
rotate=True
# precise comparison in decimal
def compare (a,b,tol=1e-15):
	if abs(a-b)<tol:
		return "equal"
	return "greater" if a>b else "less"
# Servo motor right rotation
def rightmove():
	pwm.ChangeDutyCycle(12)    				# Set the PWM duty cycle to 12% to rotate the servo to the right
	time.sleep(0.02)
	pwm.ChangeDutyCycle(0)    				# Reset the PWM duty cycle to 0% to stop the servo
	time.sleep(0.3)
# Servo motor left rotation
def leftmove():
	pwm.ChangeDutyCycle(1)					# Set the PWM duty cycle to 1% to rotate the servo to the right
	time.sleep(0.02)
	pwm.ChangeDutyCycle(0)    				# Reset the PWM duty cycle to 0% to stop the servo
	time.sleep(0.3)

def frameshow(picam2):
	frame = picam2.capture_array()    			# Capture a single frame as a numpy array from the camera
	if frame is None:    					# Check if frame capture failed (i.e., returned None)
		#print("Failed to capture image")
		return True
	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)    	# Convert the frame color from RGB (used by PiCamera) to BGR (used by OpenCV)
	cv2.namedWindow('Frame', cv2.WINDOW_NORMAL)   		# Create a window named 'Frame' for displaying the image
	cv2.setWindowProperty('Frame', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)    # Set the window to full-screen mode
	cv2.imshow('Frame', frame)    				# Display the image in the 'Frame' window
	if cv2.waitKey(1) & 0xFF == ord('q'):    		# Wait for 1 millisecond and check if the 'q' key is pressed

		return False
	return True

def show():
	while True:
			if not frameshow(picam2):		# Call the frameshow function with the picam2 object, Check the return value of the frameshow function
				break

def takepic(x,y):
	now = datetime.now()    				# Get the current date and time
	filename = now.strftime("%Y%m%d_%H%M%S")   		# Format the timestamp into a string suitable for a filename
	metadata = picam2.capture_file(f"{filename}_variance_is_{x}_resolution_is_{y}.jpg")# Capture an image file with the camera. The filename includes the current timestamp, the variance value (x), and the resolution value (y). The filename is structured as: "YYYYMMDD_HHMMSS_variance_is_X_resolution_is_Y.jpg"

def moarso(): 							# amin function to do the autofocus, "moarso" stands for MOhammad+ARash+SOheil
	initial_var=is_blurred(picam2.capture_array())		# get initial frame variance
	leftmove()						# make a left move
	second_var=is_blurred(picam2.capture_array())		# get second varince
	comp_res=compare(second_var,initial_var)		# compae second variance with initial variance to see, if it is increased(improved) or decreased(deterioration)
	# either use "rotate=False" or below if condition for better readability
	if comp_res=="greater" or comp_res=="equal":
		rotate=False #false means rotation direction is left
	else:
		rotate=True #true means rotation direction is right
	#print("initial_var",initial_var,"second_var",second_var)
	try:
		start_time = time.time()			# get time to calculate runtime
		count=0						# set number of tries
		while True:
			####### this part of code is commented because we have used an array to measure last 30 variance "line 40 & 41" to check if in last 30 variance does frame change slightly to start refocusing, then we decide that there are better solution, so we commented it
			# monitor.add_variance(is_blurred(picam2.capture_array()))
			# if monitor.is_maximum_found():
				# current_max = monitor.get_max_variance()
				# #print(f"Maximum variance in the last {window_size} frames: {current_max}")
				# picvar=is_blurred(picam2.capture_array())
				# takepic(picvar)
				# realtimevar=picvar
				# while (picvar*0.9<=realtimevar<=picvar*1.1):
					# realtimevar=is_blurred(picam2.capture_array())
			if rotate==True:			# based on the previouse rotation set, if it was TRUE, we do right rotation, and calculate new variance 
				rightmove()
				initial_var=second_var
				second_var=is_blurred(picam2.capture_array())
				print("if rotate==True: , second_var: ",second_var,"     initial_var: ",initial_var)
				comp_res=compare(second_var,initial_var)
				if comp_res=="greater" or comp_res=="equal":# Then compare it with recent varince if it increased, means we are rotating correctly, else change the rotation direction
					rotate=True
				else:
					rotate=False
					count+=1
			if rotate==False:			# based on the previouse rotation set, if it was FALSE, we do left rotation, and calculate new variance 
				leftmove()
				initial_var=second_var
				second_var=is_blurred(picam2.capture_array())
				print("if rotate==False: , second_var: ",second_var,"    initial_var:",initial_var)
				comp_res=compare(second_var,initial_var)
				if comp_res=="greater" or comp_res=="equal":# Then compare it with recent varince if it increased, means we are rotating correctly, else change the rotation direction
					rotate=False
				else:
					rotate=True
					count+=1
			if count>5:				# If it change direction 5 times, then it meanse we reached to optimum variance value, where either direction will not have any imrovement
				picvar=is_blurred(picam2.capture_array())# calculate variance
				takepic(picvar,size_str)	# Take a picture
				realtimevar=picvar		# get vaiance of the taken photo
				count=0				# Set count to 0, because if frame changed, it has to readjust the lens for better focus
				end_time = time.time()		# Set end time
				runtime = end_time - start_time	# calculate runtime
				print(f"The runtime of the code is {runtime} seconds.")
				print("change now")		# testcase print, which let you know things are finished, now you can moved or add objects 
				while (picvar*0.9<=realtimevar<=picvar*1.1): # check if variance changed by 0.1 percent
					realtimevar=is_blurred(picam2.capture_array()) # continusly check variance
				time.sleep(5)
				start_time = time.time() # Reset the start_time
			#print(f"count is {count}")

	except KeyboardInterrupt:
		print("Interrupted by user.")

	# Stop and close all the initiated component, motor, GPIO, Camera and open windows
	finally:
		pwm.stop()
		GPIO.cleanup()
		picam2.stop()
		picam2.close()
		cv2.destroyAllWindows()

# Threading to run Frame viewer without lag and in parallel obtaion optimal focused frame
focuse_thread = threading.Thread(target=moarso)
frameshow_thread = threading.Thread(target=show)
focuse_thread.start()
frameshow_thread.start()
