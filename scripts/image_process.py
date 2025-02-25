import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

def decode_base64_image(base64_string):
    """Decode base64 string to image"""
    try:
        # Remove header if present
        if 'base64,' in base64_string:
            base64_string = base64_string.split('base64,')[1]
        
        # Decode base64 string
        img_data = base64.b64decode(base64_string)
        
        # Convert to numpy array
        nparr = np.frombuffer(img_data, np.uint8)
        
        # Decode image
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img
    except Exception as e:
        print(f"Error decoding image: {str(e)}")
        return None

def preprocess_image(image, target_size=(224, 224)):
    """Preprocess image for AI model input"""
    try:
        # Convert to PIL Image
        if isinstance(image, np.ndarray):
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        # Resize
        image = image.resize(target_size, Image.LANCZOS)
        
        # Convert to numpy array and normalize
        img_array = np.array(image) / 255.0
        
        return img_array
    except Exception as e:
        print(f"Error preprocessing image: {str(e)}")
        return None

def encode_image(image):
    """Encode image to base64 string"""
    try:
        # Convert numpy array to PIL Image if needed
        if isinstance(image, np.ndarray):
            image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        # Save image to bytes buffer
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        
        # Encode to base64
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    except Exception as e:
        print(f"Error encoding image: {str(e)}")
        return None

def enhance_image(image):
    """Enhance image quality"""
    try:
        # Convert to LAB color space
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        
        # Split channels
        l, a, b = cv2.split(lab)
        
        # Apply CLAHE to L channel
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
        cl = clahe.apply(l)
        
        # Merge channels
        limg = cv2.merge((cl,a,b))
        
        # Convert back to BGR
        enhanced = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
        
        return enhanced
    except Exception as e:
        print(f"Error enhancing image: {str(e)}")
        return image  # Return original image if enhancement fails