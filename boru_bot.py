from bs4 import BeautifulSoup
import requests
import pandas as pd
import speech_recognition as sr
import pyttsx3
import sys
import random
from subprocess import Popen
import pyautogui
import random
import os


def ss_al():
    os.chdir("C:\\Users\\dogu2\\Desktop\\screenshots")
    file_name = random.randint(0,99999)
    screenshot = pyautogui.screenshot()
    pyautogui.screenshot(str(file_name)+".jpg")
    print("SS ALINDI")
    j.jarvis("SS Alındı")
def sozluk():
    p = Popen("sesli-sozluk.bat", cwd=r"C:\\Users\\dogu2\\Desktop")
    stdout, stderr = p.communicate()    

def hava_durumu(city):
    url = requests.get("http://www.hurriyet.com.tr/hava-durumu/"+city+"/")
    content = url.content
    soup = BeautifulSoup(content, "html.parser")

    today = soup.find("div", class_="today-weather-r")
    days = soup.find_all("div", class_="weather-box swiper-slide")
    for day in days:
        yazı = day.text
        new_yazı = yazı.replace("ºC", "derece")
        print(new_yazı)
        j.jarvis(new_yazı)

def bugün_hava_durumu(city):
    url = requests.get("http://www.hurriyet.com.tr/hava-durumu/" +city+ "/")
    content = url.content
    soup = BeautifulSoup(content, "html.parser")

    today = soup.find("div", class_="today-weather-r")
    days = soup.find_all("div", class_="weather-box swiper-slide")
    bugun = today.getText()
    print(bugun)
    j.jarvis(bugun)

def kapat():
    j.jarvis("görüşmek üzere...")
    print("SARVIS durduruldu")
    sys.exit()

class JARVIS:
    def listener(self,recognizer, microphone):
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source,phrase_time_limit=3)
            command = recognizer.recognize_google(audio, language="tr-TR")
            return command

    def jarvis(self,command):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        voices = engine.getProperty('voices')
        engine.setProperty("rate", 130)
        tolga = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_trTR_Tolga"
        engine.setProperty('voice', tolga)
        engine.say(command)
        engine.runAndWait()

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

j = JARVIS()

j.jarvis("Hoşgeldiniz")
j.jarvis("Dinliyorum")
def main():
    while True:
        print("Dinliyorum")
        try:
            rec = j.listener(recognizer,microphone)
            if rec == "hava durumu":
                j.jarvis("Hangi şehir ?")
                print("Hangi şehir ?")
                city = j.listener(recognizer,microphone)
                hava_durumu(city)
            if rec == "bugün hava durumu":
                j.jarvis("Hangi şehir ?")
                print("Hangi şehir ?")
                city = j.listener(recognizer, microphone)
                bugün_hava_durumu(city)
            if rec == "kapat":
                kapat()
            if rec == "sözlük":
                sozluk()
            if rec == "kaydet":
                ss_al()

        except sr.UnknownValueError:
            print("Anlayamadım.Tekrar söyler misin ?")

main()
