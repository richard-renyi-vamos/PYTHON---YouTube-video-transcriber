from pytube import YouTube
from pydub import AudioSegment
import speech_recognition as sr

def download_audio(youtube_url):
    yt = YouTube(youtube_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file = audio_stream.download(filename='audio.mp4')

    # Convert mp4 audio to wav format for speech recognition
    audio = AudioSegment.from_file(audio_file, format="mp4")
    audio.export("audio.wav", format="wav")

    return "audio.wav"

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)

    # Transcribe the audio using Google's free service
    try:
        text = recognizer.recognize_google(audio)
        print("Transcription: ", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    
    return text

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    audio_file = download_audio(youtube_url)
    transcription = transcribe_audio(audio_file)
    print("Final Transcription:", transcription)
