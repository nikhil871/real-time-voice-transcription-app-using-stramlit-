# You should see a web app running in your browser with a "Start Transcription" button. Click the button to start recording your voice, and then click the "Stop Transcription" button to stop recording and perform the transcription. The transcription will be displayed below the buttons.
# Make sure you have the required packages installed (streamlit, sounddevice, soundfile, speech_recognition). You can install them using pip:
# Save the script in a file with a .py extension (e.g., voice_transcription.py) and run it using the following command:
import streamlit as st
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

# Set up Streamlit app title and description
st.title("Real-time Voice Transcription")
st.write("Speak into your microphone and see the transcription!")

# Set up variables
filename = "temp.wav"
transcription = ""

# Define the Streamlit app function
def app():
    global transcription
    if st.button("Start Transcription"):
        # Clear previous transcription
        transcription = ""

        # Initialize the microphone recording
        with sf.SoundFile(filename, mode='w', samplerate=44100, channels=1) as file:
            with sd.InputStream(samplerate=44100, channels=1, callback=callback):
                st.write("Recording started...")
                st.write("Listening...")

                # Continuously transcribe audio until the user stops the recording
                while True:
                    if st.button("Stop Transcription"):
                        break

        # Perform transcription on the recorded audio
        r = sr.Recognizer()
        audio_data = sr.AudioFile(filename)
        with audio_data as source:
            audio = r.record(source)
            transcription = r.recognize_google(audio)

    # Display the transcription
    st.write("Transcription:")
    st.write(transcription)

# Define the callback function to save the recorded audio
def callback(indata, frames, time, status):
    if status:
        print(status)
    sf.write(filename, indata, frames)

# Run the Streamlit app
if __name__ == "__main__":
    app()
