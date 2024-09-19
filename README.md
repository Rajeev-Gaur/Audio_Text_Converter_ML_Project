# Audio to Text Converter Project

## Overview
The Audio to Text Converter is a Python-based application designed to convert Hindi audio files into editable text. The project utilizes speech recognition libraries to transcribe audio and allows for easy access to the transcribed content in a Word document format.

## Features
- Transcribes Hindi audio files (`.mp3` and `.wav`) to text.
- Outputs the transcribed text into a `.docx` file for easy editing.
- Supports both original audio input and optional synthesized audio output.

## Directory Structure
Audio_Text_Converter_ML_Project/
│
├── myenv/                         # Virtual environment folder
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
│
├── audio_files/                   # Folder for audio files
│   ├── hindi.mp3                  # Original input audio file
│   └── hindi.wav                  # Transcribed output audio file (if applicable)
│
├── transcriptions/                 # Folder for output text files
│   └── transcribed_hindi_text.docx # Output transcription file
│
├── src/                           # Folder for Python source files
│   ├── audio_to_text.py           # Main script for audio to text conversion
│   └── open_word.py               # Script to open .docx files
│
├── requirements.txt                # File listing project dependencies
│
└── README.md                       # Project documentation file

## Installation

### Prerequisites
- Python 3.6 or higher
- Pip (Python package installer)

### Setting Up the Virtual Environment
1. Clone the repository:
   ```bash
   git clone https://github.com/rajeev-gaur/Audio_Text_Converter_ML_Project.git
   cd Audio_Text_Converter_ML_Project
2. Create a virtual environment:
    python -m venv myenv
3. Activate the virtual environment:
    On Windows:
    myenv\Scripts\activate
    On macOS/Linux:
    source myenv/bin/activate
4.  Install the required packages:
    pip install -r requirements.txt

Usage:
1.Place Hindi audio file (hindi.mp3 or hindi.wav) in the audio_files directory.
2. Run the transcription script:
   python src/audio_to_text.py
3. After running the script, the transcribed text will be saved as transcribed_hindi_text.docx in the transcriptions folder.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
SpeechRecognition for audio processing.
python-docx for creating and manipulating Word documents.
audioread for handling audio file formats.

