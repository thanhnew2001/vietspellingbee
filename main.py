import csv, time
from playsound import playsound
from gtts import gTTS
import os
import speech_recognition as sr
#import pyaudio

#os.system("mpg321 welcome.mp3")

def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mời bạn nói: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="vi-VI")
            print("Bạn -->: {}".format(text))
        except:
            print("Xin lỗi! tôi không nhận được voice!")
    return text

def create_sound(text):
    tts = gTTS(text=text, lang='vi')
    tts.save("pcvoice.mp3")
    # to start the file from python
    playsound('pcvoice.mp3')

def start_read():
    file = open("tiengviet.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    page = int(input("Bạn muốn bắt đầu từ số mấy? 0-447"))
    i = 0
    for row in csvreader:
        i = i + 1
        r = row[0][2:]
        if i>page:
            words = r.split(", ")
            for w in words:
                print(w)
                # spelling_word = speechtotext()
                # if spelling_word == w:
                #     create_sound("Đúng rồi")
                # else:
                #     create_sound("Trật lất")
                playsound('bip.wav')
                #time.sleep(0.5)
                create_sound(w)
                # time.sleep(1)

    file.close()

start_read()