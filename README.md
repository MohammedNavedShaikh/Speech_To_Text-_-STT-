# Speech To Text Conversion

## Overview

The **Speech To Text Conversion** is a Flask-based web application that utilizes **OpenAI's Whisper API** to convert speech into text. The application provides both pre-recorded audio file uploads and real-time audio recording for transcription. In addition to basic transcription, the application refines and polishes the output using a **Large Language Model (LLM)** hosted on **Groq Cloud**.

## Technologies Used

- **Flask**: For creating the web application.
- **OpenAI Whisper API**: For converting speech into text.
- **Groq Cloud**: For refining and polishing the transcribed text using a language model.
- **PyAudio**: For recording real-time audio.
- **LangChain**: For advanced language model interactions.
- **Torch**: For running machine learning models.
- **Python-dotenv**: For managing environment variables.

## Features

- **Speech to Text**: Convert speech to text using OpenAI Whisper.
- **Audio Upload and Recording**: Upload pre-recorded audio files or record audio in real-time.
- **Real-time Transcription**: Display transcription of real time recorded audio.
- **Text Refinement**: The transcribed text is polished and refined using an LLM hosted on Groq Cloud.
- **Responsive Frontend**: The UI is built with HTML, CSS, and JavaScript, ensuring a smooth user experience.
- **Error Handling**: Comprehensive error handling for seamless functionality.

## Installation

Follow the steps below to set up the project locally:

### Prerequisites

- Python 3.8+
- FFmpeg for audio processing (for Windows users, Scoop is used to install it)

### 1. Clone the repository
```bash
git clone https://github.com/MohammedNavedShaikh/Speech_To_Text_Conversion.git
cd Speech_To_Text_Conversion
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux Users
venv\Scripts\activate  # Windows Users
```

### 3. Install dependencies
Install the required libraries from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory of the project and add the following keys:
```bash
GROQ_API_KEY="YOUR-GROQ-API-KEY"
```

### 5. Install FFmpeg (for Windows users)
Run the following commands to install FFmpeg via Scoop:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install ffmpeg
```

### 6. Run the application
Start the application:
```bash
python run.py
```

## How It Works

- **Audio Input**: Users can upload audio files or record audio in real-time. 
- **Whisper API**: The audio is passed through the Whisper API, which transcribes the speech into text.
- **Text Refinement**: The transcribed text is passed to a language model hosted on Groq Cloud, where it is refined and polished.
- **Real-Time Transcription**: Display transcription of real time recorded audio.
- **Frontend**: The web interface allows users to interact with the application, upload files, and view the transcriptions.

## Example Use Case

1. **Upload**: Users upload an audio file or record real-time audio.
2. **Transcription**: The speech is transcribed into text.
3. **Refinement**: The transcribed text is refined and polished using an LLM hosted on Groq Cloud.
4. **Display**: The transcribed and refined text is displayed on the webpage.

![STT-1](https://github.com/user-attachments/assets/0c84a716-05fd-4f8c-929c-eed972d273de)
![STT-2](https://github.com/user-attachments/assets/1f7a52bf-efff-4e3a-8b0e-d1b7eae41cd5)



## Project Structure
```
Speech_To_Text_Conversion/
├── app
│   ├── __pycache__
│   ├── routes
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── error_routes.py
│   │   ├── home_routes.py
│   │   ├── transcribe_routes.py
│   │   ├── upload_routes.py
│   ├── services
│   │   ├── __pycache__
│   │   ├── __init__.py
│   │   ├── refinement_service.py
│   │   ├── transcription_service.py
│   ├── static
│   │   ├── script.js
│   │   ├── styles.css
│   ├── templates
│   │   ├── 404.html
│   │   ├── index.html
│   │   ├── result.html
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── prompt.py
├── uploads
├── .env
├── config.py
├── logger.py
├── run.py
```

## Support

If you encounter any issues while setting up or using the Speech To Text Conversion application, feel free to reach out for assistance.

- **Contact**: Mohammed Naved Shaikh
- **Email**: naveds1049@gmail.com

We're here to help with any queries, bugs, or feature requests!

---
