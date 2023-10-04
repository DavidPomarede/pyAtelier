
import sys
from PIL import Image

# Open the image file
img = Image.open("drawing.png")

# Set the image size
img = img.resize((100, 100))

# Draw a red rectangle on the image
img.putalpha(1)
img.rectangle(((10, 10), (50, 50), (30, 30), (0, 0), (255, 0, 0, 255)))

# Save the image
img.save("drawing_with_rectangle.png")

