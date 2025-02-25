```
███████╗██╗ ██████╗ ██╗  ██╗████████╗    ███████╗ █████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
███████╗██║██║  ███╗███████║   ██║       ███████╗███████║██║   ██║█████╗  ██████╔╝
╚════██║██║██║   ██║██╔══██║   ██║       ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
███████║██║╚██████╔╝██║  ██║   ██║       ███████║██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
```

<div align="center">
  <img src="https://i.ibb.co/0ZgVZGn/LOGO-AIRAS.jpg" alt="AIRAS Logo" width="200"/>
  <br/>
  <a href="https://airas.godaddysites.com" target="_blank">Visit AIRAS Website</a>
</div>

# SightSaver

SightSaver is an intelligent camera system that integrates ESP32-CAM with AI-powered text-to-speech capabilities, creating a smart device that can describe what it sees.

## Features

- Real-time image capture using ESP32-CAM
- AI-powered image analysis using OpenAI's API
- Text-to-speech output for image descriptions
- Easy setup with automated scripts

## Hardware Requirements

- ESP32-CAM module
- FTDI programmer or similar USB-to-Serial adapter
- Speaker module (for TTS output)
- Micro USB cable for power and programming
- Breadboard and jumper wires

## Software Requirements

- Arduino IDE (2.0 or later)
- Python 3.7 or later
- Required Python packages (automatically installed by setup scripts)

## Setup Instructions

### Automated Setup

1. Clone this repository
2. Run the appropriate setup script for your operating system:
   - Windows: `setup.bat`
   - Linux/macOS: `setup.sh`

### Manual Setup

1. Install Arduino IDE
2. Add ESP32 board support to Arduino IDE
3. Install required Arduino libraries:
   - ESP32 Camera Driver
   - ArduinoJson
4. Install Python dependencies:
   ```
   pip install requests openai python-dotenv
   ```

## Configuration

1. Copy `config.h.example` to `config.h`
2. Update the following configurations in `config.h`:
   - WiFi credentials
   - OpenAI API key
   - Pin configurations

## Hardware Connection

1. Connect FTDI programmer to ESP32-CAM:
   - FTDI RX → ESP32-CAM TX
   - FTDI TX → ESP32-CAM RX
   - FTDI GND → ESP32-CAM GND
   - FTDI 3.3V → ESP32-CAM 3.3V
2. Connect speaker module to designated pins

## Usage

1. Upload the code to ESP32-CAM using Arduino IDE
2. Open Serial Monitor to view system status
3. Point the camera at objects/scenes
4. The system will:
   - Capture images
   - Send them for AI analysis
   - Convert descriptions to speech

## Project Structure

```
├── src/
│   ├── main.ino          # Main Arduino sketch
│   ├── camera_utils.h     # Camera handling functions
│   ├── config.h          # Configuration settings
│   ├── openai_api.h      # OpenAI API integration
│   └── tts_utils.h       # Text-to-speech functions
├── scripts/
│   ├── image_process.py  # Image processing utilities
│   └── api_handler.py    # API communication handler
├── setup.bat             # Windows setup script
├── setup.sh             # Linux/macOS setup script
└── README.md            # This file
```

## Troubleshooting

1. **Camera Won't Initialize**
   - Check power supply stability
   - Verify pin connections
   - Reset the module

2. **WiFi Connection Issues**
   - Verify credentials in config.h
   - Ensure network availability
   - Check WiFi signal strength

3. **TTS Not Working**
   - Verify speaker connections
   - Check volume settings
   - Monitor Serial output for errors

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under AIRAS Personal Use License  - see the LICENSE file for details.

## Credits

Developed by Atah Alam (Zyxciss) for AIRAS INC.
