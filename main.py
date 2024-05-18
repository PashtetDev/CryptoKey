import sys
import os
from libs.ui.main_window_ui import Ui_MainWindow
from libs.ui.support_window_ui import Ui_Dialog as Support
from libs.ui.confirm_ui import Ui_Dialog as Confirm
from libs.ui.reliability_ui import Ui_Dialog as Reliability
from libs.ui.change_pss_ui import Ui_Dialog as ChangePss
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from libs import crypto
from libs.account import Account
import subprocess
import webbrowser
import updater

try:
    import custom.custom as custom
    found = True
except ModuleNotFoundError as err:
    found = False

empty_custom = 'def custom_alg(string):\n'+\
'   new_pss = string\n'+\
'   #########################################\n\n'+\
'   #Ваш кастомный алгоритм генерации пароля#\n\n'+\
'   #########################################\n'+\
'   return new_pss\n'

def write_current_user(_login, pss):
    with open(f'{os.path.dirname(__file__)}\\libs\\data\\current_user', "w") as f:
        data = {'login': f'{_login}', 'password': f'{pss}'}
        print(str(data), file=f)


def warning_notification(msg):
    QtWidgets.QMessageBox.warning(None, "Warning!",
                                msg, QtWidgets.QMessageBox.Cancel)


class KeyManager(QMainWindow):
    def __init__(self, app):
        QMainWindow.__init__(self)
        self.app = app
        self.link_2 = None
        self.link_1 = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.object_connect()
        self.col = None
        self.current_id = None
        self.user = Account()
        self.get_news()
        self.get_current_user()

    def get_current_user(self):
        with open(f'{os.path.dirname(__file__)}\\libs\\data\\current_user', "r") as f:
            data = f.read()
            doc = eval(data)
            if doc['login'] != '':
                if self.user.login(doc['login'], doc['password']):
                    self.user.data.login = doc['login']
                    self.col = self.user.data.get_user_with_login()['collection']
                    self.open_main_window(doc['login'])
                else:
                    self.open_login_window()
                    warning_notification("Пароль или логин не совпадает!")
            else:
                self.open_login_window()

    def login(self):
        _login = self.ui.login.text()
        pss = self.ui.pss.text()
        write_current_user('', '')
        if len(_login) == 0 or len(pss) == 0:
            warning_notification('Пустая строка!')
        else:
            if self.user.login(_login, pss):
                self.user.data.login = _login
                self.col = self.user.data.get_user_with_login()['collection']
                self.open_main_window(_login)
                write_current_user(_login, pss)
            else:
                warning_notification("Пароль или логин не совпадает!")

    def object_connect(self):
        self.ui.stringEdit.textChanged.connect(self.gen_pss)
        self.ui.modelEdit.currentIndexChanged.connect(self.gen_pss)
        self.ui.tableWidget.clicked.connect(self.on_select_password)
        self.ui.loginBtn.clicked.connect(self.login)
        self.ui.toExitBtn.clicked.connect(self.open_login_window)
        self.ui.signupBtn.clicked.connect(self.open_registration_window)
        self.ui.resetPassBtn.clicked.connect(self.open_registration_window)
        self.ui.mainBtn.clicked.connect(self.open_main_page)
        self.ui.managerBtn.clicked.connect(self.open_main_page)
        self.ui.settingBtn.clicked.connect(self.open_main_page)
        self.ui.quitBtn.clicked.connect(self.quit)
        self.ui.deleteBtn.clicked.connect(self.delete_current_key)
        self.ui.delAccButton.clicked.connect(self.open_confirm_window)
        self.ui.uploadBtn.clicked.connect(self.download_data)
        self.ui.closeEditor.clicked.connect(self.close_key_editor)
        self.ui.saveBtn.clicked.connect(self.on_save_btn_clcked)
        self.ui.codeInput.textChanged.connect(self.check_code)
        self.ui.regBtn.clicked.connect(self.registration)
        self.ui.sendCodeBtn.clicked.connect(self.on_send_btn_clicked)
        self.ui.supportBtn.clicked.connect(self.open_support_window)
        self.ui.customBtn.clicked.connect(self.open_custom)
        self.ui.pssChangeBtn.clicked.connect(self.open_change_pss_window)
        self.ui.custBtn.clicked.connect(self.open_custom)
        self.ui.readBtn.clicked.connect(self.open_url)
        self.ui.readBtn2.clicked.connect(self.open_url)
        self.ui.readBtn3.clicked.connect(self.open_url)
        self.ui.moreBtn.clicked.connect(self.open_url)
        self.ui.checkBtn.clicked.connect(self.reliability_check)

        if updater.get_new_version() > updater.get_cur_version():
            self.ui.versionLabel.hide()
            self.ui.updateBtn.clicked.connect(self.update)
        else:
            self.ui.updateBtn.hide()
            with open(os.path.dirname(__file__)+"\\libs\\data\\config.txt") as f:
                self.ui.versionLabel.setText(eval(f.read())['version'])

        if found:
            self.ui.modelEdit.addItem("Кастомный")
            self.ui.customBtn.setText("Изменить кастомный алгоритм")
        else:
            self.ui.customBtn.setText("Создать кастомный алгоритм")

        self.ui.newKeyBtn.clicked.connect(self.open_key_editor)

    def update(self):
        updater.update(self, self.app)

    def reliability_check(self):
        self.new_window = QtWidgets.QDialog()
        self.reliability_window = Reliability()
        self.reliability_window.setupUi(self.new_window)
        self.reliability_window.mngBtn.clicked.connect(self.open_main_page)

        result = str(self.user.data.reliability_check())
        if result is not None:
            result = result.replace("number_flag", "наличие цифр")
            result = result.replace("upper_flag", "наличие символов в верхнем регистре")
            result = result.replace("lower_flag", "наличие символов в нижнем регистре")
            result = result.replace("special_flag", "наличие специальных символов")
            result = result.replace("time", "время подбора")
            result = result.replace("length", "длина пароля")
            words = result.split(', ')
            msg = ''
            for word in words:
                msg += word + '\n'
                if '}' in word:
                    msg += '\n'

            self.reliability_window.plainTextEdit.setPlainText(str(msg))

        self.new_window.show()

    def open_custom(self):
        if not os.path.exists(f"{os.path.dirname(__file__)}\\custom\\custom.py"):
            with open(f"{os.path.dirname(__file__)}\\custom\\custom.py", "w") as f:
                print(empty_custom, file=f)
            self.ui.customBtn.setText("Изменить кастомный алгоритм")
            self.ui.modelEdit.addItem("Кастомный")
        subprocess.Popen(f'explorer /select, "{os.path.dirname(__file__)}\\custom\\custom.py"')

    def open_support_window(self):
        self.new_window = QtWidgets.QDialog()
        self.support_window = Support()
        self.support_window.setupUi(self.new_window)
        self.support_window.sendBtn.clicked.connect(self.send_support_msg)

        self.new_window.show()

    def registration(self):
        mode = self.sender().text() == "Зарегистрироваться"
        if self.user.code_chck:
            status, msg = self.user.registration(self.ui.createPss.text(), self.ui.confPss.text(), mode)
            if status:
                self.ui.login.setText(str(self.user.data.login))
                self.open_login_window()
            else:
                warning_notification(msg)
        else:
            warning_notification('Почта не подтверждена')

    def open_change_pss_window(self):
        self.new_window = QtWidgets.QDialog()
        self.chg_pss_window = ChangePss()
        self.chg_pss_window.setupUi(self.new_window)
        self.chg_pss_window.saveBtn.clicked.connect(self.change_pss)

        self.new_window.show()

    def change_pss(self):
        status, msg = self.user.registration(self.chg_pss_window.pss.text(), self.chg_pss_window.confPss.text(), False)
        if not status:
            warning_notification(msg)
        else:
            write_current_user(self.user.data.login, self.chg_pss_window.pss.text())
            self.new_window.close()

    def send_support_msg(self):
        if self.support_window.textEdit.toPlainText() != "":
            if self.support_window.themeEdit.currentIndex() != -1:
                self.user.mail.send_email(self.support_window.textEdit.toPlainText() +
                                          f"\n\nFrom {self.user.data.login}",
                                          self.support_window.themeEdit.currentText(), "support")
            else:
                warning_notification("Выберите тему обращения")
        else:
            warning_notification("Пустое текстовое поле")

        self.new_window.close()

    def open_main_page(self):
        sender = self.sender().objectName()
        max = 16777215

        self.close_main_menu()

        if sender == "mainBtn":
            self.ui.mainPage.setMaximumSize(max, max)
        elif sender == "settingBtn":
            self.ui.settings.setMaximumSize(max, max)
        elif sender == "managerBtn":
            self.ui.passwordManager.setMaximumSize(max, max)
        else:
            self.new_window.close()
            self.ui.passwordManager.setMaximumSize(max, max)

    def open_url(self):
        sender = self.sender().objectName()
        if sender == "readBtn":
            webbrowser.open(self.link_1)
        elif sender == "readBtn2":
            webbrowser.open(self.link_2)
        elif sender == "readBtn3":
            webbrowser.open("https://habr.com/ru/companies/globalsign/articles/697708/")
        elif sender == "moreBtn":
            webbrowser.open("https://habr.com/ru/companies/cloud4y/articles/347952/")

    def get_news(self):
        news, links, authors = self.user.data.get_last_news()
        if news[0] is not None and links[0] is not None and authors[0] is not None:
            self.ui.newsTitle.setPlainText(news[0])
            self.ui.from1.setText(authors[0])
            self.link_1 = links[0]
            if news[1] is not None and links[1] is not None and authors[1] is not None:
                self.ui.newsTitle2.setPlainText(news[1])
                self.ui.from2.setText(authors[1])
                self.link_2 = links[1]
        else:
            self.link_1 = "https://habr.com/ru/companies/dataline/articles/563228/"
            self.link_2 = "https://habr.com/ru/articles/336578/"


    def close_key_editor(self):
        self.ui.tableWidget.clearSelection()
        self.ui.keyEditor.setMaximumSize(300, 0)
        self.ui.deleteBtn.hide()

    def on_save_btn_clcked(self):
        if self.sender().text() == "Сохранить":
            self.add_key()
        else:
            self.update_key()

    def open_key_editor(self):
        self.ui.stringEdit.setText('')
        if self.sender().objectName() == 'newKeyBtn':
            self.ui.keyEditor.setMaximumSize(300, 450)
            self.ui.saveBtn.setText("Сохранить")
            self.ui.password.setText('Пароль')
            self.ui.titleEdit.setText('')
            self.ui.deleteBtn.hide()
            self.ui.tableWidget.clearSelection()
        else:
            self.ui.saveBtn.setText("Изменить")
            if len(self.ui.tableWidget.selectedItems()) > 0:
                self.ui.keyEditor.setMaximumSize(300, 450)
                index = self.ui.tableWidget.selectedItems()[0].row()
                self.current_id = self.keys[index]['id']
                self.ui.password.setText(self.keys[index]['password'])
                self.ui.titleEdit.setText(self.keys[index]['title'])
            else:
                warning_notification("Не выбрана ни одна запись")

    def add_key(self):
        if len(self.ui.stringEdit.text()) == 0 or len(self.ui.titleEdit.text()) == 0:
            warning_notification("Обнаружены пустые строки!")
        else:
            if self.ui.password.text() == "Пароль":
                warning_notification("Сгенерируйте пароль!")
            else:
                data = {
                    'password': f'{self.ui.password.text()}',
                    'title': f'{self.ui.titleEdit.text()}',
                    'collection': f'{self.col}'
                }
                self.user.data.create_key(data)
                self.close_key_editor()
                self.view_data()

    def update_key(self):
        new_data = {
            'password': f'{self.ui.password.text()}',
            'title': f'{self.ui.titleEdit.text()}',
            'collection': f'{self.col}'
        }
        self.user.data.update_existing_key(self.current_id, new_data)
        self.close_key_editor()
        self.view_data()

    def delete_current_key(self):
        if len(self.ui.tableWidget.selectedItems()) > 0:
            index = self.ui.tableWidget.selectedItems()[0].row()
            self.user.data.delete_key(self.keys[index]['id'])
            self.close_key_editor()
            self.view_data()
        else:
            warning_notification("Не выбрана ни одна запись")

    def gen_pss(self):
        input_str = self.ui.stringEdit.text()
        if len(input_str) == 0:
            self.ui.password.setText("Пароль")
        else:
            model = self.ui.modelEdit.currentText()

            if model == 'Простой':
                pss = crypto.simple_alg(input_str)
            elif model == 'Сильный':
                pss = crypto.strong_alg(input_str)
            elif model == 'Кастомный':
                pss = custom.custom_alg(input_str)
            else:
                pss = input_str

            self.ui.password.setText(pss)

    def close_main_menu(self):
        self.ui.mainPage.setMaximumSize(0, 0)
        self.ui.settings.setMaximumSize(0, 0)
        self.ui.passwordManager.setMaximumSize(0, 0)

    def open_main_window(self, login):
        max = 16777215

        self.close_general()
        self.close_key_editor()
        self.close_main_menu()
        self.ui.username.setText(login)
        self.ui.general.setMaximumSize(max, max)
        self.ui.mainPage.setMaximumSize(max, max)
        self.ui.loginMenu.setMaximumSize(0, 0)
        self.ui.regMenu.setMaximumSize(0, 0)
        self.ui.deleteBtn.hide()
        self.view_data()

    def on_select_password(self):
        if len(self.ui.tableWidget.selectedItems()) > 0:
            self.open_key_editor()
            self.ui.deleteBtn.show()
        else:
            self.close_key_editor()

    def open_confirm_window(self):
        self.new_window = QtWidgets.QDialog()
        self.confirm_window = Confirm()
        self.confirm_window.setupUi(self.new_window)
        self.confirm_window.buttonBox.accepted.connect(self.delete_account)
        self.confirm_window.buttonBox.rejected.connect(self.new_window.close)

        self.new_window.show()

    def on_send_btn_clicked(self):
        if self.sender().text() == "Отправить код":
            self.ui.sendCodeBtn.clicked.connect(self.send_code)
        else:
            self.ui.sendCodeBtn.clicked.connect(self.send_reset_code)

    def open_registration_window(self):
        sizeX = 500
        max = 16777215
        sender = self.sender().objectName()
        self.close_general()
        self.ui.general.setMinimumSize(0, 0)
        self.ui.loginMenu.setMinimumSize(0, 0)
        self.ui.regMenu.setMaximumSize(max, max)
        self.ui.regMenu.setMinimumSize(sizeX, 0)

        if sender == 'signupBtn':
            self.ui.regBtn.setText("Зарегистрироваться")
            self.ui.sendCodeBtn.setText("Отправить код")
        else:
            self.ui.regBtn.setText("Сменить пароль")
            self.ui.sendCodeBtn.setText("Отправить код сброса")

    def send_code(self):
        email = self.ui.email.text()
        self.user.data.login = email
        status, msg = self.user.send_code(email)
        if not status:
            warning_notification(msg)
            self.ui.login.setText(email)

    def send_reset_code(self):
        email = self.ui.email.text()
        status, msg = self.user.send_reset_code(email)
        if not status:
            warning_notification(msg)
            self.ui.login.setText(email)

    def check_code(self):
        if self.user.code is not None:
            status, msg = self.user.code_check(self.ui.codeInput.text(), self.ui.email.text())
            if status:
                self.ui.emailCheck.setCheckable(True)
                self.ui.emailCheck.setChecked(True)
                self.ui.email.setReadOnly(True)
                self.ui.codeInput.setReadOnly(True)

    def open_login_window(self):
        sizeX = 500
        max = 16777215

        self.close_general()
        self.ui.general.setMinimumSize(0, 0)
        self.ui.loginMenu.setMaximumSize(max, max)
        self.ui.loginMenu.setMinimumSize(sizeX, 0)
        self.ui.regMenu.setMinimumSize(0, 0)

    def close_general(self):
        self.ui.general.setMaximumSize(0, 0)
        self.ui.general.setMinimumSize(0, 0)
        self.ui.loginMenu.setMaximumSize(0, 0)
        self.ui.loginMenu.setMinimumSize(0, 0)
        self.ui.regMenu.setMaximumSize(0, 0)
        self.ui.regMenu.setMinimumSize(0, 0)

    def view_data(self):
        col = self.col
        if col is not None:
            self.keys = self.user.data.get_all_docs()

            row = 0
            self.ui.tableWidget.setRowCount(len(self.keys))
            for key in self.keys:
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key['title']))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(key['password']))
                row += 1

    def quit(self):
        write_current_user('', '')
        self.col = None
        self.user.data.login = ''
        self.current_id = None
        self.get_current_user()

    def download_data(self):
        data = self.user.data.get_all_docs()
        msg = "Список паролей:\n"

        for key in data:
            msg += f'Название: {key["title"]}, Пароль: {key["password"]}\n'

        self.user.mail.send_email(msg, "Выгрузка паролей", self.user.data.login)

    def delete_account(self):
        self.download_data()
        for key in self.keys:
            self.user.data.delete_key(key['id'])

        self.user.data.delete_user()
        self.quit()


def __init():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    window = KeyManager(app)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    __init()