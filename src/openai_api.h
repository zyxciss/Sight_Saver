/*
 * Project: ESP32-CAM AI TTS Integration
 * Author: Atah Alam (Zyxciss)
 * Organization: AIRAS INC.
 * 
 * This file contains functions for OpenRouter API integration
 */

#ifndef OPENAI_API_H
#define OPENAI_API_H

#include <Arduino.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include "config.h"

/**
 * Send image URL to OpenRouter API and get description
 * @param image_url The URL of the captured image
 * @return String containing the API response (image description)
 */
String sendImageToOpenAI(String image_url) {
    HTTPClient http;
    String response = "";
    
    // OpenRouter API endpoint
    http.begin("https://openrouter.ai/api/v1");
    
    // Set headers
    http.addHeader("Content-Type", "application/json");
    http.addHeader("Authorization", String("Bearer ") + OPENROUTER_API_KEY);
    
    // Create JSON payload
    StaticJsonDocument<1024> doc;
    doc["model"] = "qwen/qwen-vl-plus:free";
    
    JsonArray messages = doc.createNestedArray("messages");
    JsonObject message = messages.createNestedObject();
    message["role"] = "user";
    
    JsonArray content = message.createNestedArray("content");
    
    JsonObject textContent = content.createNestedObject();
    textContent["type"] = "text";
    textContent["text"] = "What is in this image?";
    
    JsonObject imageContent = content.createNestedObject();
    imageContent["type"] = "image_url";
    JsonObject imageUrl = imageContent.createNestedObject("image_url");
    imageUrl["url"] = image_url;
    
    String jsonString;
    serializeJson(doc, jsonString);
    
    // Send POST request
    int httpResponseCode = http.POST(jsonString);
    
    if (httpResponseCode > 0) {
        response = http.getString();
        
        // Parse response to get description
        StaticJsonDocument<1024> responseDoc;
        DeserializationError error = deserializeJson(responseDoc, response);
        
        if (!error) {
            if (responseDoc.containsKey("choices") && 
                responseDoc["choices"][0].containsKey("message") && 
                responseDoc["choices"][0]["message"].containsKey("content")) {
                response = responseDoc["choices"][0]["message"]["content"].as<String>();
            }
        }
    } else {
        Serial.print("Error on sending POST: ");
        Serial.println(httpResponseCode);
        response = "Error: Failed to get image description";
    }
    
    http.end();
    return response;
}

#endif // OPENAI_API_H