import os
from dotenv import load_dotenv
import gradio as gr
from skryba import Scryba

load_dotenv()

def process(input_audio, input_youtube, language, temperature, top_p, max_output_tokens):
    result = Scryba().pipeline(input_audio, input_youtube, language, temperature, top_p, max_output_tokens)
    return result

with gr.Blocks(title="Skryba - AI-powered tool to transcribes and summarizes your audio files and recordings", theme="base") as interface:
    gr.Markdown(
    """
    # Skryba
    Skryba is a tool that transcribes and summarizes audio files or YouTube clips. 
    """)
    with gr.Row():
        with gr.Column():
            with gr.Tab(label="Input"):
                with gr.Group():
                    input_audio = gr.Audio(type="filepath", label="Upload or record an audio file", editable=False)
            with gr.Tab(label="Youtube"):
                with gr.Group():
                    input_youtube = gr.TextArea(label="Paste youtube link")
            with gr.Tab(label="Additional settings"):
                with gr.Group():
                    language = gr.Radio(["Polish", "English"], value="Polish", label="Output language")
                    max_output_tokens = gr.Number(value=500, label="Maximum output tokens", minimum=1, maximum=1000)  
                    temperature = gr.Slider(value=0.2, label="Temperature", minimum=0.0, maximum=1.0, step=0.1)
                    top_p = gr.Slider(value=0.9, label="Top P", minimum=0.1, maximum=1.0, step=0.1)
        with gr.Column():
            with gr.Tab(label="Summary"):
                with gr.Group():
                    summary = gr.Markdown(container=True, min_height="40vh", max_height="40vh")
            with gr.Tab(label="Transcription file"):
                with gr.Group():
                    file = gr.File(scale=1)
    with gr.Row():
        clear_button = gr.ClearButton(icon="static/icons/clear.png")
        process_button = gr.Button(icon="static/icons/process.png")

    process_button.click(process, inputs=[input_audio, input_youtube, language, temperature, top_p, max_output_tokens], outputs=[summary, file])
    clear_button.click(lambda: [None, None, None, None], outputs=[input_audio, input_youtube, summary, file])

if __name__ == "__main__":
    interface.launch(pwa=True, share=False, inbrowser=True)