import os
import sys
import shutil
import time

import requests
import zipfile


url = 'https://github.com/PashtetDev/CryptoKey/archive/refs/heads/master.zip'
dir_name = os.path.dirname(__file__)
file_path = dir_name + "\\Crypto.zip"


def update(window, app):
    try:
        import main
        try:
            app.quit()
        except AttributeError:
            print("Что-то пошло не так O.O")
    except ModuleNotFoundError:
        print("Что-то пошло не так O.O")


    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)

        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(dir_name)
        os.remove(file_path)

        if os.path.exists(dir_name + "\\libs"):
            shutil.rmtree(dir_name + "\\libs")
        if os.path.exists(dir_name + "\\main.py"):
            os.remove(dir_name + "\\main.py")

        source = f"{dir_name}\\CryptoKey-master"
        destination = f"{dir_name}"
        shutil.move(source + "\\libs", destination)
        shutil.move(source + "\\main.py", destination + "\\main.py")
        shutil.rmtree(source)

    open_main()


def open_main():
    try:
        import main
        try:
            main.__init()
        except AttributeError:
            print("Что-то пошло не так O.O")
    except ModuleNotFoundError:
        print("Что-то пошло не так O.O")


def get_cur_version():
    if os.path.exists(dir_name + "\\libs\\data\\config.txt"):
        with open(dir_name + "\\libs\\data\\config.txt", 'r') as file:
            string = eval(file.read())
            return int(string['version'].split('.')[3])
    else:
        return 0


def get_new_version():
    response = requests.get('https://github.com/PashtetDev/CryptoKey/blob/master/libs/data/config')
    if response.status_code == 200:
        src = response.text
        index = src.find('version\':')
        version = int(src[index+10:index+25].split('.')[3])
        return version
    else:
        return 0