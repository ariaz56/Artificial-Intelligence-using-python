from transformers import pipeline
from PIL import Image

# Load pre-trained image captioning model
captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base"
)

# Enter image file name
image_path = input("Enter image path: ")

# Open image
image = Image.open(image_path)

# Generate caption
result = captioner(image)

# Display caption
print("\nImage Caption:")
print(result[0]["generated_text"])