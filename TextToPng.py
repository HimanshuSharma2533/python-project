# pip install opencv-python
import cv2
import numpy as np

# Input text
text = "Hello, this is my handwriting app!"

# Create a white canvas (height, width, channels)
image = np.ones((300, 800, 3), dtype=np.uint8) * 255

# Set font, scale, color, and thickness
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
font_scale = 1
color = (0, 0, 0)  # Black
thickness = 2

# Put text on the image
cv2.putText(image, text, (50, 150), font, font_scale, color, thickness, cv2.LINE_AA)

# Save the image
cv2.imwrite("handwriting_output.png", image)

print("Handwriting image saved as handwriting_output.png")