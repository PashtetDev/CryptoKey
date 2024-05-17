import os
import shutil
import requests
import zipfile


url = 'https://github.com/PashtetDev/CryptoKey/archive/refs/heads/master.zip'
dir_name = os.path.dirname(__file__)
file_path = dir_name + "\\Crypto.zip"


def update():
    response = requests.get(url)

    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(dir_name)

        if os.path.exists(dir_name + "\\libs"):
            shutil.rmtree(dir_name + "\\libs")
        if os.path.exists(dir_name + "\\main.py"):
            os.remove(dir_name + "\\main.py")

        source = f"{dir_name}\\CryptoKey-master"
        destination = f"{dir_name}"
        shutil.move(source + "\\libs", destination)
        shutil.move(source + "\\main.py", destination+"\\main.py")

        shutil.rmtree(source)
        os.remove(file_path)

        print('File downloaded successfully')
        try:
            import main
            try:
                main.__init()
            except AttributeError:
                print("Что-то пошло не так O.O")
        except ModuleNotFoundError:
            print("Что-то пошло не так O.O")
    else:
        print('Failed to download file')


if __name__ == "__main__":
    update()