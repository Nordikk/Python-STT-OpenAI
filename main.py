import openai
import tkinter as tk
from tkinter import filedialog
from dotenv import load_dotenv
import os

def transcribe_audio(file_path):
    # Load the API key from the .env file
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

def format_and_summarize(text):
    # Format the text into paragraphs and generate a summary using GPT-3.5-turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text},
            {"role": "assistant", "content": "Please format the above text into paragraphs and then (additionally) provide a summary. The original text should be present. Do it in the original language of the text, which is most likely german."},
        ]
    )

    # Extract the generated text from the response
    formatted_text = response["choices"][0]["message"]["content"].strip()

    return formatted_text

def main():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Open a file dialog for selecting the MP3 file
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

    # Transcribe the audio file
    text = transcribe_audio(file_path)

    # Write the transcribed text to a text file
    with open(file_path.rsplit(".", 1)[0] + ".txt", "w", encoding="utf-8") as text_file:
        text_file.write(text)

    # Ask the user whether they want to format and summarize the text
    if tk.messagebox.askyesno("Format and Summarize", "Do you want to format and summarize the transcribed text?"):
        # Read the transcribed text from the text file
        with open(file_path.rsplit(".", 1)[0] + ".txt", "r", encoding="utf-8") as text_file:
            text = text_file.read()

        # Format and summarize the text
        text = format_and_summarize(text)

        # Write the formatted and summarized text to a new text file
        with open(file_path.rsplit(".", 1)[0] + "-summary.txt", "w", encoding="utf-8") as text_file:
            text_file.write(text)

# Run the main function
if __name__ == "__main__":
    main()
