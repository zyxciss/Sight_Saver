/*
 * Project: ESP32-CAM AI TTS Integration
 * Author: Atah Alam (Zyxciss)
 * Organization: AIRAS INC.
 * 
 * Main Arduino sketch that initializes the camera, connects to WiFi,
 * and orchestrates the image capture, API analysis, and TTS output workflow.
 */

#include <WiFi.h>
#include "config.h"
#include "camera_utils.h"
#include "openai_api.h"
#include "tts_utils.h"

void setup() {
    // Initialize serial communication
    Serial.begin(115200);
    Serial.println("\nESP32-CAM AI TTS Integration");

    // Connect to WiFi
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
    Serial.print("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWiFi connected");

    // Initialize camera
    if (!initCamera()) {
        Serial.println("Camera initialization failed");
        return;
    }
    Serial.println("Camera initialized successfully");
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        // Capture and upload image
        String imageUrl = captureAndUploadImage();
        Serial.println("Image URL: " + imageUrl);

        // Send image to OpenRouter API for analysis
        String description = sendImageToOpenAI(imageUrl);
        Serial.println("Image description: " + description);

        // Convert description to speech
        speak(description);
    } else {
        Serial.println("WiFi connection lost");
    }

    // Wait before next iteration
    delay(LOOP_DELAY);
}