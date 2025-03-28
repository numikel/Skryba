# 🧠 Skryba

**Skryba** is an AI-powered Python tool that transcribes and summarizes audio files or YouTube videos using OpenAI’s Whisper and GPT-4o(-mini).  
It's useful for processing meeting recordings, lectures, educational videos, and voice notes — either from your device or directly from YouTube.

---

## 🚀 Features

- ✅ Transcribes `.mp3` and other audio files  
- ✅ Supports direct transcription from YouTube links (no pre-download needed)  
- ✅ Summarizes in **Polish** or **English** using `gpt-4o-mini` or other choosen model 
- ✅ Saves transcription to a `.txt` file  
- ✅ Easy-to-use Gradio web interface  
- ✅ Supports recording via browser microphone (requires `ffmpeg`)  

---

## 🛠 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a .env file in the project root:

```ini
OPENAI_API_KEY=your_openai_key
```

---
## ▶️ How to Use
###💻 Script/Dev Mode
You can call Skryba directly from Python:

```python
from skryba import Scryba

scryba = Scryba()

# From audio file
summary, transcript_path = scryba.pipeline(audio_path="your_audio.mp3")

# From YouTube link
summary, transcript_path = scryba.pipeline(youtube_path="https://www.youtube.com/watch?v=dQw4w9WgXcQ")

print(summary)
```
---
## 🌐 Web Interface
Launch the interface:

```bash
python main.py
```

You will be able to:
1) Upload or record an audio file or paste a YouTube link
2) Choose output language and adjust summarization parameters
3) View the summary and download the transcription

🎤 Microphone support requires ffmpeg
To use microphone recording in the Gradio web UI, ffmpeg must be installed and available in your system PATH.

🔧 Download it from:
https://www.gyan.dev/ffmpeg/builds/

After downloading:
1) Extract it (e.g., to `C:\ffmpeg`)
2) Add `C:\ffmpeg\bin` to your system environment variable PATH
3) Restart your terminal
4) You can test installation by running:

```bash
ffmpeg -version
```

## ⚙️ Parameters
| Parameter           | Description                                        | Default         |
|--------------------|----------------------------------------------------|-----------------|
| `audio_path`        | Path to a local audio file                         | `None`          |
| `youtube_path`      | YouTube URL for downloading audio and transcribing | `None`          |
| `language`          | Output language for the summary                    | `"polish"`      |
| `temperature`       | Controls randomness of the model's response        | `0.2`           |
| `top_p`             | Nucleus sampling parameter                         | `0.9`           |
| `max_output_tokens` | Maximum length of the generated summary (tokens)   | `500`           |
| `model`             | OpenAI model used for summarization                | `"gpt-4o-mini"` |

## 📁 Project Structure
```bash
skryba/
├── skryba.py               # Main logic (download, transcribe, summarize)
├── main.py                  # Gradio-based web UI
├── requirements.txt        # Dependencies
├── .env                    # Environment variables
├── temp/                   # Folder for temporary transcription/audio files
└── static/icons/           # UI icons for buttons
```

### 📌 To-do
1) Add language auto-detection
2) Add transcription editor in UI

## 👤 Author
Made with 🧠 by Michał Kamiński

