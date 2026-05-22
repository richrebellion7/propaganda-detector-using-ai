import easyocr
import numpy as np
from PIL import Image


reader = easyocr.Reader(['en'])


def extract_text_from_image(uploaded_file):

    image = Image.open(uploaded_file).convert("RGB")

    image_array = np.array(image)

    results = reader.readtext(image_array)

    extracted_text = " ".join([result[1] for result in results])

    return extracted_text