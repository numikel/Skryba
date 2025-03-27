import os
from dotenv import load_dotenv
from openai import OpenAI
import datetime as dt

load_dotenv()

class Scryba():
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def pipeline(self, audio_path, language = 'polish', temperature = 0.3, top_p = 0.9, max_output_tokens=250, model = "gpt-4o"):
        transcription = self.transcribe(audio_path)
        return self.summarize(transcription, language, model, temperature, top_p, max_output_tokens)

    def transcribe(self, audio_path):
        with open(audio_path, 'rb') as audio:
            response = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio,
            )

        transcription = response.text

        return transcription

    def summarize(self, transcription, language = 'polish', model = "gpt-4o", temperature = 0.3, top_p = 0.9, max_output_tokens=250):
        response = self.client.responses.create(
            model=model,
            input=transcription,
            instructions=f"Summarize the transcription in a structured format (e.g., bullet points or a concise paragraph). If the transcription is in a different language than {language}, translate it and provide the answer in {language}. If the transcription is already in {language}, summarize it directly in the same language",
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
    
    def get_current_time(self):
        return dt.datetime.now().strftime("%Y%m%d%H%M%S")

if __name__ == "__main__":
    scryba = Scryba()
    print(scryba.pipeline("test2.mp3"))