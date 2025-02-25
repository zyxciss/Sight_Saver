// Constants
const BACKEND_URL = 'http://localhost:8000';

// DOM Elements
const capturedImage = document.getElementById('captured-image');
const noImageText = document.getElementById('no-image');
const imageDescription = document.getElementById('image-description');
const audioPlayer = document.getElementById('audio-player');
const noAudioText = document.getElementById('no-audio');
const statusMessage = document.getElementById('status-message');

// Function to update the UI with new image and description
async function processImage(imageUrl) {
    try {
        // Update status
        statusMessage.textContent = 'Processing image...';
        
        // Show image
        capturedImage.src = imageUrl;
        capturedImage.style.display = 'block';
        noImageText.style.display = 'none';
        
        // Send image to backend for analysis
        const response = await fetch(`${BACKEND_URL}/analyze-image`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image_url: imageUrl })
        });
        
        if (!response.ok) {
            throw new Error('Failed to analyze image');
        }
        
        const data = await response.json();
        
        // Update description
        imageDescription.textContent = data.description;
        
        // Update audio player
        audioPlayer.src = `${BACKEND_URL}/audio/${data.audio_file.split('/').pop()}`;
        audioPlayer.style.display = 'block';
        noAudioText.style.display = 'none';
        
        // Update status
        statusMessage.textContent = 'Processing complete';
        
    } catch (error) {
        console.error('Error:', error);
        statusMessage.textContent = `Error: ${error.message}`;
    }
}

// Function to simulate receiving an image from ESP32-CAM
// In a real implementation, this would be triggered by a WebSocket message or server-sent event
function simulateImageCapture() {
    const demoImageUrl = 'https://example.com/captured_image.jpg';
    processImage(demoImageUrl);
}

// For demo purposes, simulate image capture every 30 seconds
setInterval(simulateImageCapture, 30000);