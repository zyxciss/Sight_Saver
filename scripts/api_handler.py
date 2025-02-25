import os
import json
import requests
from dotenv import load_dotenv
from image_process import encode_image

# Load environment variables
load_dotenv()

class OpenAIHandler:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        self.vision_url = 'https://api.openai.com/v1/chat/completions'
    
    def analyze_image(self, image):
        """Analyze image using OpenAI's Vision API"""
        try:
            # Encode image to base64
            base64_image = encode_image(image)
            if not base64_image:
                raise ValueError("Failed to encode image")
            
            # Prepare the request payload
            payload = {
                "model": "gpt-4-vision-preview",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": "What do you see in this image? Provide a concise description."
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": 300
            }
            
            # Make the API request
            response = requests.post(self.vision_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            # Extract and return the description
            result = response.json()
            description = result['choices'][0]['message']['content']
            return description.strip()
            
        except Exception as e:
            print(f"Error analyzing image: {str(e)}")
            return None

    def generate_speech(self, text):
        """Generate speech from text using OpenAI's TTS API"""
        try:
            tts_url = 'https://api.openai.com/v1/audio/speech'
            payload = {
                "model": "tts-1",
                "input": text,
                "voice": "alloy"
            }
            
            response = requests.post(tts_url, headers=self.headers, json=payload)
            response.raise_for_status()
            
            return response.content
            
        except Exception as e:
            print(f"Error generating speech: {str(e)}")
            return None