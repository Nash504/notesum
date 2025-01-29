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
    YOU ARE A TRANSCRIPTION AND SUMMARIZATION MODEL.
    Summarize the input audio(which usually conists of actions) into bullet points.  
     Focus on preserving the core ideas in a concise and clear way. 
    """
    
    # Generate content from the uploaded file
    result = model.generate_content([myfile, var])
    print(f"Transcription: {result.text}")

    # Clean the result text further using the model
    response = model.generate_content(f"{result.text}")
    print(f"Cleaned Transcription: {response.text}")
    
    # Delete the uploaded audio file after processing
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_path}")
    
    return response.text  # Return the transcribed text
