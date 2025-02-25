#!/bin/bash

echo
echo "███████╗██╗ ██████╗ ██╗  ██╗████████╗    ███████╗ █████╗ ██╗   ██╗███████╗██████╗ "
echo "██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗"
echo "███████╗██║██║  ███╗███████║   ██║       ███████╗███████║██║   ██║█████╗  ██████╔╝"
echo "╚════██║██║██║   ██║██╔══██║   ██║       ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗"
echo "███████║██║╚██████╔╝██║  ██║   ██║       ███████║██║  ██║ ╚████╔╝ ███████╗██║  ██║"
echo "╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝"
echo
echo "Setting up SightSaver project environment..."

# Check for Python installation
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Installing Python..."
    if [[ "$(uname)" == "Darwin" ]]; then
        # macOS
        brew install python3
    elif [[ -f /etc/debian_version ]]; then
        # Debian/Ubuntu
        sudo apt-get update
        sudo apt-get install -y python3 python3-pip
    elif [[ -f /etc/redhat-release ]]; then
        # RHEL/CentOS/Fedora
        sudo dnf install -y python3 python3-pip
    else
        echo "Unable to detect package manager. Please install Python 3.7 or later manually."
        exit 1
    fi
fi

# Check for pip
if ! command -v pip3 &> /dev/null; then
    echo "pip is not installed! Please install pip."
    exit 1
fi

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install opencv-python numpy pillow requests python-dotenv

# Create .env file template
echo "Creating .env file template..."
echo "OPENAI_API_KEY=your_api_key_here" > .env

# Check for Arduino IDE
if ! command -v arduino &> /dev/null; then
    echo "Arduino IDE not found. Installing Arduino IDE..."
    if [[ "$(uname)" == "Darwin" ]]; then
        # macOS
        brew install --cask arduino
    elif [[ -f /etc/debian_version ]]; then
        # Debian/Ubuntu
        sudo apt-get update
        sudo apt-get install -y arduino
    elif [[ -f /etc/redhat-release ]]; then
        # RHEL/CentOS/Fedora
        sudo dnf install -y arduino
    else
        echo "Please install Arduino IDE manually from https://www.arduino.cc/en/software"
    fi
fi

# Check for Arduino CLI
if ! command -v arduino-cli &> /dev/null; then
    echo "Installing Arduino CLI..."
    curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh
    export PATH=$PATH:$HOME/bin
fi

# Install ESP32 board support
echo "Installing ESP32 board support..."
arduino-cli core install esp32:esp32

# Install required libraries
echo "Installing Arduino libraries..."
arduino-cli lib install "ESP32 Camera"
arduino-cli lib install "ArduinoJson"

# Install esptool for flashing
echo "Installing esptool for ESP32 flashing..."
pip install esptool

echo "Setup completed successfully!"
echo "Please update your OpenAI API key in the .env file."

# Make the script executable
chmod +x setup.sh