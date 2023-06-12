import openai
import tkinter as tk
from tkinter import filedialog
from dotenv import load_dotenv
import os

def transcribe_audio(file_path):
    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = api_key
    
    # Open the audio file
    audio_file = open(file_path, "rb")
    
    # Transcribe the audio file
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    
    # Extract the text from the response
    text = transcript["text"]
    
    # Close the audio file
    audio_file.close()
    
    return text

def main():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()
    
    # Open a file dialog for selecting the MP3 file
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    
    # Transcribe the audio file
    text = transcribe_audio(file_path)
    
    # Write the transcribed text to a text file
    with open(file_path.rsplit(".", 1)[0] + ".txt", "w") as text_file:
        text_file.write(text)
        
# Run the main function
if __name__ == "__main__":
    main()
    