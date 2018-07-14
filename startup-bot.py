# -*- coding: utf-8 -*-

import speech_recognition as sr
import urllib3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import webbrowser
import sys
import os

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

        if command == "kapat":
            print(command)
            print("durduruldu")
            sys.exit()
        elif command == "sayfalar":
            print(command)
            for sayfa in urls:
                webbrowser.open_new_tab(sayfa)
                print(sayfa+" açılıyor...")
        elif command == "güç":
            print("güle güleeee")
            os.system("shutdown -s")
        if command == "arama":
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
