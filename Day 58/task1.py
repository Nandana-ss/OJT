import cv2
import matplotlib.pyplot as plt
from PIL import Image
import imageio

# Load an image using OpenCV
image_path = "apple.jpeg"
image_cv2 = cv2.imread(image_path)

# Convert the image from BGR to RGB for proper display
image_cv2_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)

# Display the image loaded with OpenCV
plt.imshow(image_cv2_rgb)
plt.title('Image loaded with OpenCV')
plt.axis('off')  # Hide the axis
plt.show()

# Load an image using PIL
image_pil = Image.open(image_path)

# Display the image loaded with PIL
plt.imshow(image_pil)
plt.title('Image loaded with PIL')
plt.axis('off')  # Hide the axis
plt.show()

# Load an image using imageio
image_imageio = imageio.imread(image_path)

# Display the image loaded with imageio
plt.imshow(image_imageio)
plt.title('Image loaded with imageio')
plt.axis('off')  # Hide the axis
plt.show()

# Define path for JPG images
image_path_jpg = "logo.jpg"

# OpenCV
image_cv2_jpg = cv2.imread(image_path_jpg)
image_cv2_jpg_rgb = cv2.cvtColor(image_cv2_jpg, cv2.COLOR_BGR2RGB)
plt.imshow(image_cv2_jpg_rgb)
plt.title('JPG loaded with OpenCV')
plt.axis('off')  # Hide the axis
plt.show()

# PIL
image_pil_jpg = Image.open(image_path_jpg)
plt.imshow(image_pil_jpg)
plt.title('JPG loaded with PIL')
plt.axis('off')  # Hide the axis
plt.show()

# imageio
image_imageio_jpg = imageio.imread(image_path_jpg)
plt.imshow(image_imageio_jpg)
plt.title('JPG loaded with imageio')
plt.axis('off')  # Hide the axis
plt.show()
