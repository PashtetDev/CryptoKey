import os
import sys
import shutil
import time

import requests
import zipfile


url = 'https://github.com/PashtetDev/CryptoKey/archive/refs/heads/master.zip'
dir_name = os.path.dirname(__file__)
file_path = dir_name + "\\Crypto.zip"


def update():
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(dir_name)
    os.remove(file_path)

    with open(os.path.dirname(__file__) + "\\libs\\data\\current_user", 'r') as f:
        cur_user = f.read()

    if os.path.exists(dir_name + "\\libs"):
        shutil.rmtree(dir_name + "\\libs")
    if os.path.exists(dir_name + "\\ui_resources"):
        shutil.rmtree(dir_name + "\\ui_resources")
    if os.path.exists(dir_name + "\\main.pyw"):
        os.remove(dir_name + "\\main.pyw")

    source = f"{dir_name}\\CryptoKey-master"
    destination = f"{dir_name}"
    shutil.move(source + "\\libs", destination)
    shutil.move(source + "\\ui_resources", destination)
    shutil.move(source + "\\main.pyw", destination + "\\main.pyw")
    shutil.move(source + "\\updater.py", destination + "\\updater_1.py")
    shutil.rmtree(source)

    with open(os.path.dirname(__file__) + "\\libs\\data\\current_user", 'w') as f:
        print(cur_user, file=f)

    open_main()


def download():
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)


def open_main():
    os.startfile(os.path.dirname(__file__) + "\\main.pyw")
    sys.exit()


def check_update():
    if os.path.exists(dir_name + "\\libs\\data\\config"):
        with open(dir_name + "\\libs\\data\\config", 'r') as file:
            string = eval(file.read())
            version = int(string['version'].split('.')[3])
            if version < get_new_version():
                download()
                return True
    else:
        return False


def get_new_version():
    response = requests.get('https://github.com/PashtetDev/CryptoKey/blob/master/libs/data/config')
    if response.status_code == 200:
        src = response.text
        index = src.find('version\':')
        version = int(src[index+10:index+25].split('.')[3])
        return version
    else:
        return 0
