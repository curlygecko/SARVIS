# -*- coding: utf-8 -*-

import speech_recognition as sr
import urllib3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import webbrowser
import os
import pandas as pd
from bs4 import BeautifulSoup
import requests



def hava():
    url = requests.get("https://www.ntvhava.com/konum/eskisehir/3-gunluk-hava-tahmini")
    content = url.content
    soup = BeautifulSoup(content, "html.parser")

    günler = soup.find_all("div", class_="date")
    sıcaklıklar = soup.find_all("span", class_="range2 font25")
    sıcak = []
    for sıcaklık in sıcaklıklar:
        sıcak.append(sıcaklık.getText())
    del sıcak[1]
    del sıcak[2]
    del sıcak[3]

    tablo = {"-----Gün-----": [],
             "Sıcaklık": []}

    for gün, sıc in zip(günler, sıcak):
        tablo["-----Gün-----"].append(gün.getText())
        tablo["Sıcaklık"].append(sıc)

    data = pd.DataFrame(tablo)
    print(data)


urls = ["https://www.reddit.com/","https://www.youtube.com/","https://www.google.com/"]
print("***************SARVIS V1.0***************")
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum... >> ")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, phrase_time_limit=5)

    try:
        command = r.recognize_google(audio,key=None, language="tr-TR")

        if "kapat" in command:
            print(command)
            print("durduruldu")
            sys.exit()
        elif command == "sayfalar":
            print(command)
            for sayfa in urls:
                webbrowser.open_new_tab(sayfa)
                print(sayfa+" açılıyor...")
        elif "hava durumu" in command:
            hava()
        elif command == "kaydet":
            try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("Yazmak için dinliyorum... ")
                        r.adjust_for_ambient_noise(source, duration=1)
                        audio = r.listen(source, phrase_time_limit=10)
                    command_yaz = r.recognize_google(audio, key=None, language="tr-TR")
                    os.chdir("C:\\Users\\dogu2\\Desktop\\")
                    with open("yazıcı.txt", "w", encoding="utf-8") as yazdır:
                        yazdır.write(command_yaz)
                        yazdır.close()
            except sr.UnknownValueError:
                print("Anlaşılmadı..")
        elif command == "oku":
            metin = open("yazıcı.txt", "r", encoding="utf-8")
            okut = metin.read()
            print(okut)
        if "arama" in command:
            driver = webdriver.Chrome()
            driver.get("https://www.google.com/")
            ara = driver.find_element_by_class_name("gsfi")
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print("Aranacak şeyi söyle ")
                    r.adjust_for_ambient_noise(source, duration=1)
                    audio = r.listen(source, phrase_time_limit=5)

                    command_ara = r.recognize_google(audio, key=None, language="tr-TR")
                    ara.send_keys(command_ara)
                    ara.send_keys(Keys.ENTER)

            except sr.UnknownValueError:
                print("Tekrar söyle")



    except sr.UnknownValueError:
        print("Anlaşılmadı.Tekrar dene")
