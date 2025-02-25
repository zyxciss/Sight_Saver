from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from openai import OpenAI
import httpx
import os
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your_api_key_here")
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
AUDIO_OUTPUT_DIR = "audio_output"

# Create audio output directory if it doesn't exist
os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)

class ImageRequest(BaseModel):
    image_url: str

@app.post("/analyze-image")
async def analyze_image(request: ImageRequest):
    try:
        # Send image to OpenRouter API for analysis
        async with httpx.AsyncClient() as client:
            response = await client.post(
                OPENROUTER_API_URL,
                headers={
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "qwen/qwen-vl-plus:free",
                    "messages": [
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "What is in this image?"},
                                {"type": "image_url", "image_url": {"url": request.image_url}}
                            ]
                        }
                    ]
                }
            )
            
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Failed to analyze image")
            
        analysis_result = response.json()
        description = analysis_result["choices"][0]["message"]["content"]
        
        # Generate audio from description using Kokoro TTS
        client = OpenAI(base_url='https://api.kokorotts.com/v1', api_key='not-needed')
        audio_file = f"{AUDIO_OUTPUT_DIR}/output_{os.urandom(4).hex()}.mp3"
        
        response = client.audio.speech.create(
            model='kokoro',
            voice='af_bella+af_sky',
            input=description,
            response_format='mp3'
        )
        
        response.stream_to_file(audio_file)
        
        return {
            "description": description,
            "audio_file": audio_file
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/audio/{filename}")
async def get_audio(filename: str):
    file_path = os.path.join(AUDIO_OUTPUT_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Audio file not found")
    return FileResponse(file_path, media_type="audio/mpeg")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)