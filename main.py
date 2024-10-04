import pyttsx3
import speech_recognition as sr
import pyaudio
import csv

def data_set(text):
    with open('badwords.csv', mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        bad_words = [row[0] for row in reader]

    for bad_word in bad_words:
        text = text.replace(bad_word, "beep")
    return text
r = sr.Recognizer()
a = 1
with sr.Microphone() as source:
    while a:
        print("Please say something")
        try:
            audio = r.listen(source)
            voice_data = r.recognize_google(audio)
            print("You said:", voice_data)
            x = data_set(voice_data)
            print("Processed Output:", x)
            pyobj = pyttsx3.init()
            pyobj.say(x)
            pyobj.runAndWait()
        except Exception as e:
            print("Error:", e)
        a = int(input("Press 1 to continue or 0 to exit: "))
