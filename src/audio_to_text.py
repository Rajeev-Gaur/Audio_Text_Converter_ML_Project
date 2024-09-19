import speech_recognition as sr
import os
from docx import Document  # Make sure to install python-docx

def recognize_audio(audio_file):
    recognizer = sr.Recognizer()

    # Check if the audio file exists
    if not os.path.exists(audio_file):
        return f"Error: The audio file '{audio_file}' does not exist."

    print(f"Recording audio from: {audio_file}")  # Debugging line

    try:
        with sr.AudioFile(audio_file) as source:
            print("Audio file opened successfully.")  # Debugging line
            audio_data = recognizer.record(source)
            print("Audio data recorded successfully.")  # Debugging line
            
            # Attempt to recognize the audio
            print("Recognizing audio...")  # Debugging line
            text = recognizer.recognize_google(audio_data, language='hi-IN')  # Specify Hindi language
            print("Text recognized successfully.")  # Debugging line
            return text
    except sr.UnknownValueError:
        return "Error: Google Speech Recognition could not understand the audio."
    except sr.RequestError as e:
        return f"Error: Could not request results from Google Speech Recognition service; {e}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def save_to_docx(text, filename):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
    print(f"Text written to {filename}")

if __name__ == "__main__":
    audio_file = r'C:\Users\DeLL\Desktop\Visual Studio Coding\Audio_Text_Converter_ML_Project\output_hindi.wav'  # Replace with your WAV file path
    
    transcribed_text = recognize_audio(audio_file)
    print("Transcribed Text:", transcribed_text)  # Print the output directly

    # Save to a DOCX file
    if "Error" not in transcribed_text:
        save_to_docx(transcribed_text, r'C:\Users\DeLL\Desktop\Visual Studio Coding\Audio_Text_Converter_ML_Project\transcribed_hindi_text.docx')










