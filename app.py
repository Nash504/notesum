import google.generativeai as genai
from audio import record_audio
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("API_KEY")
genai.configure(api_key=api_key)
record_audio()
myfile = genai.upload_file("output.wav")

model = genai.GenerativeModel("gemini-1.5-flash")
var = """
Definition
YOU ARE A TRANSCRIPTION AND SUMMARIZATION MODEL NOTHING BEYOND THAT.
Summarize the input text by identifying the main points and removing unnecessary details, 
filler words, and repetition. Focus on preserving the core ideas in a concise and clear way. 
Keep the summary short and direct.Make them bullet points.Nothing more nothing less.DO NOT PROVIDE YOUR OWN OPINION JUST GIVE ME THE BULLET POINTS.'
"""
result = model.generate_content([myfile, var])
model = genai.GenerativeModel("gemini-1.5-flash")
print(f"{result.text=}")
response = model.generate_content(f"{result.text}")
print(f"Clean data: {response.text}")
