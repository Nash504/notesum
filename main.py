from flask import Flask, render_template, request, jsonify
import os
from app import transcribe_and_summarize  # Import the transcribe function from app.py

app = Flask(__name__)

# Set up a folder to store the uploaded audio files
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store transcriptions globally (use a more persistent storage in a production app)
transcriptions = []

# Allow only .wav files
ALLOWED_EXTENSIONS = {'wav'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    # Render the index.html file located in the templates folder
    return render_template('index.html', transcriptions=transcriptions)

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No file part"}), 400

    audio_file = request.files['audio']
    
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if audio_file and allowed_file(audio_file.filename):
        # Save the uploaded file
        filename = os.path.join(UPLOAD_FOLDER, 'recording.wav')
        audio_file.save(filename)

        # Call the transcribe_and_summarize function with the saved file
        transcription = transcribe_and_summarize(filename)  # Pass the file path

        # Store transcription in the global variable
        transcriptions.append(transcription)

        # Return the updated transcription list to frontend
        return jsonify({"message": "Audio file uploaded and transcribed successfully", "transcription": transcription, "all_transcriptions": transcriptions}), 200
    else:
        return jsonify({"error": "Invalid file type"}), 400
    home()

if __name__ == '__main__':
    app.run(debug=True)
