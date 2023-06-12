# 🎙️ Speech-to-Text Transcription Tool 📝

This tool is primarily designed to transcribe audio messages from WhatsApp or iMessage. It uses the OpenAI Speech-to-Text API (Whisper) to transcribe audio files and the OpenAI GPT-3.5-turbo model to format the transcribed text into paragraphs and generate a summary.

## 🚀 Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or later
- pip (Python package installer)

### Installation

1. Clone the repository or download the Python script and the `.env` file to your local machine.

```bash
git clone https://github.com/Nordikk/Python-STT-OpenAI.git
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key in the .env file:

```env
OPENAI_API_KEY=your_api_key_here
```

## 🎯 Usage

Run the Python script:
```bash
python main.py
```
The program will open a file dialog for you to select an MP3 file. After you select a file, it will transcribe the audio and write the transcribed text to a text file in the same directory as the MP3 file.

Then, the program will ask you whether you want to format and summarize the transcribed text. If you click "Yes", it will use the GPT-3.5-turbo model to format the text into paragraphs and generate a summary, and then write the formatted and summarized text to a new text file with a "-summary" suffix in the same directory as the MP3 file.

## 📝 Note

The quality of the transcription and the formatting and summarizing of the text may vary depending on the quality and content of the audio file. The program works best with clear, high-quality audio in a supported language.

## 📜 License

This project is licensed under the terms of the MIT license.
