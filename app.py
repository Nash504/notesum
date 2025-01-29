import google.generativeai as genai
from dotenv import load_dotenv
import os

def transcribe_and_summarize(file_path):
    load_dotenv()
    api_key = os.getenv("API_KEY")
    genai.configure(api_key=api_key)

    # Upload the file to the Gemini AI API
    myfile = genai.upload_file(file_path)

    # Define the transcription model and input parameters
    model = genai.GenerativeModel("gemini-1.5-flash")
    var = """
    Definition
    YOU ARE A TRANSCRIPTION AND SUMMARIZATION MODEL NOTHING BEYOND THAT.
    Summarize the input text by identifying the main points and removing unnecessary details, 
    filler words, and repetition. Focus on preserving the core ideas in a concise and clear way. 
    Keep the summary short and direct.Make them bullet points.Nothing more nothing less.DO NOT PROVIDE YOUR OWN OPINION JUST GIVE ME THE BULLET POINTS.'
    """
    
    # Generate content from the uploaded file
    result = model.generate_content([myfile, var])
    print(f"Transcription: {result.text}")

    # Clean the result text further using the model
    response = model.generate_content(f"{result.text}")
    print(f"Cleaned Transcription: {response.text}")
    
    return response.text  # Return the transcribed text
