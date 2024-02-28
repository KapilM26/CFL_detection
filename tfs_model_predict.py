import requests
import json
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt

# Load the JPG image
image_path = "C:/Users/kgrna/Downloads/Kartik/Kartik/ELG5902/CFL_training_data-20240207T044725Z-001/CFL_training_data/input/VesselD20H15_0.jpg"

image = cv2.resize(cv2.imread(image_path), (256,256))
image_array = np.array(image)#.reshape(1, 256, 256, 3) / 255.0

# image_array = np.array(image) / 255.0
image_array=np.expand_dims(image_array,axis=0)

# image = Image.open(image_path)
print(np.array(image_array).shape)
# # Convert the image to a NumPy array
# image_array = np.array(image).reshape(1, 256, 256, 3) / 255.0  # Normalize to [0, 1]


# Create JSON data for the request
data = json.dumps({"signature_name": "serving_default", "instances": image_array.tolist()})

# Send POST request to TensorFlow Serving API
url = "http://localhost:8501/v1/models/saved_model:predict"
headers = {"content-type": "application/json"}
response = requests.post(url, data=data, headers=headers)


# Assuming the response contains the image data in a 'predictions' field
predictions = response.json()['predictions']
predictions_array = np.array(predictions)
print(predictions_array[predictions_array>=0.5])
# print(predictions_array[0].shape)
# predictions_array[predictions_array>=0.5] = 1
# predictions_array[predictions_array<0.5] = 0
# print(predictions_array)
predictions_array = predictions_array.reshape(256,256)
# Convert predictions to a NumPy array
# image_array = np.array(predictions).reshape(256,256,1)

# image = Image.fromarray((predictions_array[0] * 255).astype(np.uint8))

# # image.save("output_image.jpg")

# image.show()


# # Compute the histogram
# hist, bin_edges = np.histogram(image_array * 255, bins='auto')

# # Plot the histogram
# plt.hist(image_array)
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram of Data')
# plt.grid(True)
# plt.show()

plt.imshow(predictions_array, cmap='gray')  # 'gray' colormap for grayscale images
# plt.imshow(image_array[0], cmap='gray')  # 'gray' colormap for grayscale images

# # Add colorbar for reference
plt.colorbar()

# # Customize the plot
# plt.title('2D Array Visualization')
# plt.xlabel('Column Index')
# plt.ylabel('Row Index')

# # Display the plot
plt.show()






