import cv2
import numpy as np

# Create a 512x512 grayscale image
width, height = 512, 512
channels = 3
image = np.zeros((height, width, channels), dtype=np.uint8)

print(image)
# Fill the image with a gradient
for c in range(channels):
    for y in range(height):
        for x in range(width):
            random_value = np.random.randint(0, 256, dtype=np.uint8)
            image[y, x, c] = random_value

print(f"image = {image}")
# Save the image
cv2.imwrite('grayscale_image.png', image)

# Display the image
cv2.imshow('Grayscale Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
