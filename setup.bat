@echo off
echo.
echo ███████╗██╗ ██████╗ ██╗  ██╗████████╗    ███████╗ █████╗ ██╗   ██╗███████╗██████╗ 
echo ██╔════╝██║██╔════╝ ██║  ██║╚══██╔══╝    ██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
echo ███████╗██║██║  ███╗███████║   ██║       ███████╗███████║██║   ██║█████╗  ██████╔╝
echo ╚════██║██║██║   ██║██╔══██║   ██║       ╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
echo ███████║██║╚██████╔╝██║  ██║   ██║       ███████║██║  ██║ ╚████╔╝ ███████╗██║  ██║
echo ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝       ╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
echo.
echo Setting up SightSaver project environment...

:: Check for Python installation
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading Python 3.11.4...
    curl -o python_installer.exe https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe
    echo Installing Python...
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
    echo Python installation completed.
)

:: Check for pip
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed! Please install pip.
    exit /b 1
)

:: Create and activate virtual environment
echo Creating virtual environment...
python -m venv venv
call .\venv\Scripts\activate

:: Install Python dependencies
echo Installing Python dependencies...
pip install opencv-python numpy pillow requests python-dotenv

:: Create .env file template
echo Creating .env file template...
echo OPENAI_API_KEY=your_api_key_here > .env

:: Check for Arduino IDE
where arduino >nul 2>&1
if %errorlevel% neq 0 (
    echo Arduino IDE not found. Downloading Arduino IDE...
    curl -o arduino_installer.exe https://downloads.arduino.cc/arduino-ide/arduino-ide_2.1.1_Windows_64bit.exe
    echo Installing Arduino IDE...
    arduino_installer.exe /SILENT
    del arduino_installer.exe
    echo Arduino IDE installation completed.
)

:: Check for Arduino CLI
arduino-cli version >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing Arduino CLI...
    curl -o arduino-cli.exe https://downloads.arduino.cc/arduino-cli/arduino-cli_latest_Windows_64bit.exe
    move arduino-cli.exe %USERPROFILE%\AppData\Local\Arduino15\arduino-cli.exe
    setx PATH "%PATH%;%USERPROFILE%\AppData\Local\Arduino15"
    echo Arduino CLI installation completed.
)

:: Install ESP32 board support
echo Installing ESP32 board support...
arduino-cli core install esp32:esp32

:: Install required libraries
echo Installing Arduino libraries...
arduino-cli lib install "ESP32 Camera"
arduino-cli lib install "ArduinoJson"

:: Install esptool for flashing
echo Installing esptool for ESP32 flashing...
pip install esptool

echo Setup completed successfully!
echo Please update your OpenAI API key in the .env file.
pause