# Speech To Text Conversion

## Overview
Speech_To_Text_Conversion is a Flask-based web application that provides a platform to convert speech into text using OpenAI's Whisper API. The project incorporates additional features such as transcription refinement and dynamic handling of audio uploads.

## Features
- Convert speech to text using OpenAI Whisper.
- Users can upload pre-recorded audio files or record audio in real-time.
- Real-time transcription of audio to textual format.
- Refined and polished text output using a Large Language Model (LLM) hosted on Grooq Cloud.
- Modern, responsive frontend built with HTML, CSS, and JavaScript.
- Error handling for seamless user experience.

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

## Libraries Used
Install the required libraries:

```
pip install flask flask-cors openai whisper pyaudio
pip install git+https://github.com/openai/whisper.git
pip install langchain-groq
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install python-dotenv
```

## Installation Instructions
### Prerequisites
1. Python installed on your system.
2. [Scoop](https://scoop.sh/) and FFmpeg installed via PowerShell:

   ```
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
   scoop install ffmpeg
   ```

### Steps
1. Clone the repository:
   ```
   git clone https://github.com/MohammedNavedShaikh/Speech_To_Text_Conversion.git
   cd Speech_To_Text_Conversion
   ```
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Create a .env file and add necessary environment variables.
   ```
   GROQ_API_KEY="YOUR-GROQ-API-KEY"
   ```
6. Run the application:
   ```
   python run.py
   ```

## Usage
1. Open a browser and navigate to `http://127.0.0.1:5000`.
2. Upload an audio file or record audio in real-time for transcription.
3. View the transcribed text.
4. Obtain a refined and polished version of the text powered by the LLM hosted on Grooq Cloud.

## Contributing
Feel free to submit issues or pull requests for improvements.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- OpenAI for the Whisper model.
- Grooq Cloud for hosting the LLM.
- Flask for the web framework.
- LangChain for enabling advanced language model interactions.

---

Enjoy using Speech_To_Text_Conversion! 😊

