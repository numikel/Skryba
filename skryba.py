import os
from dotenv import load_dotenv
from openai import OpenAI
import datetime as dt
import yt_dlp

load_dotenv()

class Scryba():
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def pipeline(self, audio_path = None, youtube_path = None, language = 'polish', temperature = 0.3, top_p = 0.9, max_output_tokens=250, model = "gpt-4o-mini"):
        if (youtube_path):
            audio_path = self.get_youtube_audio(youtube_path)
            transcription = self.transcribe(audio_path)
            self.remove_temp_file(audio_path)
        elif (audio_path):
            transcription = self.transcribe(audio_path)
        else:
            return None
        return self.summarize(transcription, language, model, temperature, top_p, max_output_tokens)

    def get_youtube_audio(self, youtube_path):
        output_path = f"temp/{self.get_current_time()}_yt_audio.webm"
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'postprocessors': [],
            'quiet': True,
        }   

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(youtube_path)

        return output_path

    def transcribe(self, audio_path):
        with open(audio_path, 'rb') as audio:
            response = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio,
            )

        transcription = response.text

        return transcription

    def summarize(self, transcription, language = 'polish', model = "gpt-4o", temperature = 0.3, top_p = 0.9, max_output_tokens=500):
        response = self.client.responses.create(
            model=model,
            input=transcription,
            instructions=f"Summarize the transcription in easy to read form. If the transcription is in a different language than {language}, translate it and provide the answer in {language}. If the transcription is already in {language}, summarize it directly in the same language",
            temperature=temperature,
            top_p=top_p,
            max_output_tokens=max_output_tokens
        )

        summary = response.output[0].content[0].text 
        file_path = f"temp/transcription_{self.get_current_time()}.txt"        
        f = open(file_path, "w")
        f.write(transcription)
        f.close()
        
        return summary, file_path
    
    def remove_temp_file(self, path):
        if os.path.exists(path):
            os.remove(path)
            return True

        return False

    def get_current_time(self):
        return dt.datetime.now().strftime("%Y%m%d%H%M%S")

if __name__ == "__main__":
    pass