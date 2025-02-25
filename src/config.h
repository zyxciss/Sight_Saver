/*
 * Project: ESP32-CAM AI TTS Integration
 * Author: Atah Alam (Zyxciss)
 * Organization: AIRAS INC.
 * 
 * This file contains configuration settings for WiFi and API credentials.
 * Update these values with your actual credentials before uploading to the device.
 */

#ifndef CONFIG_H
#define CONFIG_H

// WiFi credentials
#define WIFI_SSID "your_wifi_ssid"        // Replace with your WiFi network name
#define WIFI_PASSWORD "your_wifi_password"  // Replace with your WiFi password

// OpenRouter API configuration
#define OPENROUTER_API_KEY "your_api_key"   // Replace with your OpenRouter API key

// API endpoint configuration
#define OPENROUTER_API_URL "https://openrouter.ai/api/v1"  // OpenRouter API endpoint
#define OPENROUTER_MODEL "qwen/qwen-vl-plus:free"         // Model to use for image analysis

// System configuration
#define LOOP_DELAY 15000  // Delay between iterations (15 seconds)

#endif // CONFIG_H