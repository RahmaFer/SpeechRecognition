# This is a sample Python script.
import deepgram
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import speech_recognition as sr
pause_flag = False

def pause():
    global pause_flag
    pause_flag = True

def resume():
    global pause_flag
    pause_flag = False


def save_transcribed_text(transcribed_text, filename):
    with open(filename, 'w') as file:
        file.write(transcribed_text)
def transcribe_speech(paus,rsm,language):

    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:

        try:
            if paus==True:
                return "Transcription paused. Use the 'resume()' function to resume the process."
            elif rsm==True:
                st.info("Speak now...")
                # listen for speech and store in audio_text variable
                audio_text = r.listen(source)
                st.info("Transcribing...")
                text = r.recognize_google(audio_text,language=language)
                # Save Transcribed text into a file
                filename = "transcription.txt"
                save_transcribed_text(text, filename)
                return text
            else:
                st.info("Speak now...")
                # listen for speech and store in audio_text variable
                audio_text = r.listen(source)
                st.info("Transcribing...")
                text = r.recognize_google(audio_text,language=language)
                # Save Transcribed text into a file
                filename = "transcription.txt"
                save_transcribed_text(text, filename)
                return text



        except sr.UnknownValueError:
            return "Speech recognition could not understand You."

        except sr.RequestError:
            return "Could not connect to the speech recognition service."


def main():
    st.title("Speech Recognition App")
    language = st.selectbox("Please choose the language you want to speak with: ",['en-US', 'French'])
    st.write("Click on the microphone to start speaking:")
    # add a button to trigger speech recognition
    record=st.button("Start Recording")
    paus  = st.button("Pause")
    rsm=st.button("Resume")
    if record:
        text = transcribe_speech(False,False,language)
        st.write("Transcription: ", text)
    if paus:
        text = transcribe_speech(True, False,language)
    if rsm:
        text = transcribe_speech(False, True,language)
        st.write("Transcription: ", text)



if __name__ == '__main__':
    main()


