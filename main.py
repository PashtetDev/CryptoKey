import sys
import os
from libs.ui.main_window_ui import Ui_MainWindow
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from libs import crypto
from libs.account import Account


def write_current_user(_login, pss):
    with open(f'{os.path.dirname(__file__)}\\libs\\data\\current_user', "w") as f:
        data = {'login': f'{_login}', 'password': f'{pss}'}
        print(str(data), file=f)


def warning_notification(msg):
    QtWidgets.QMessageBox.warning(None, "Warning!",
                                msg, QtWidgets.QMessageBox.Cancel)


class KeyManager(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.buttons_connect()
        self.col = None
        self.current_id = None
        self.user = Account()
        self.get_current_user()

    def get_current_user(self):
        with open(f'{os.path.dirname(__file__)}\\libs\\data\\current_user', "r") as f:
            data = f.read()
            doc = eval(data)
            if doc['login'] != '':
                if self.user.login(doc['login'], doc['password']):
                    self.user.user_data.login = doc['login']
                    self.col = self.user.user_data.get_user_with_login()['collection']
                    self.open_main_window(doc['login'])
                else:
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
                self.user.user_data.login = _login
                self.col = self.user.user_data.get_user_with_login()['collection']
                self.open_main_window(_login)
                write_current_user(_login, pss)
            else:
                warning_notification("Пароль или логин не совпадает!")

    def buttons_connect(self):
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
        self.ui.delAccButton.clicked.connect(self.delete_account)
        self.ui.uploadBtn.clicked.connect(self.download_data)

        self.ui.newKeyBtn.clicked.connect(self.open_key_editor)


    def open_main_page(self):
        sender = self.sender().objectName()
        max = 16777215

        self.close_main_menu()

        if sender == "mainBtn":
            self.ui.mainPage.setMaximumSize(max, max)
        elif sender == "settingBtn":
            self.ui.settings.setMaximumSize(max, max)
        else:
            self.ui.passwordManager.setMaximumSize(max, max)

    def close_key_editor(self):
        self.ui.tableWidget.clearSelection()
        self.ui.keyEditor.setMaximumSize(300, 0)
        self.ui.deleteBtn.hide()

    def open_key_editor(self):
        self.ui.generateBtn.clicked.connect(self.gen_pss)
        self.ui.stringEdit.setText('')
        self.ui.closeEditor.clicked.connect(self.close_key_editor)
        if self.sender().objectName() == 'newKeyBtn':
            self.ui.keyEditor.setMaximumSize(300, 450)
            self.ui.saveBtn.clicked.connect(self.add_key)
            self.ui.saveBtn.setText("Сохранить")
            self.ui.password.setText('Пароль')
            self.ui.titleEdit.setText('')
            self.ui.deleteBtn.hide()
            self.ui.tableWidget.clearSelection()
        else:
            self.ui.saveBtn.setText("Изменить")
            self.ui.saveBtn.clicked.connect(self.update_key)
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
                self.user.user_data.create_key(data)
                self.close_key_editor()
                self.view_data()

    def update_key(self):
        new_data = {
            'password': f'{self.ui.password.text()}',
            'title': f'{self.ui.titleEdit.text()}',
            'collection': f'{self.col}'
        }
        self.user.user_data.update_existing_key(self.current_id, new_data)
        self.close_key_editor()
        self.view_data()

    def delete_current_key(self):
        if len(self.ui.tableWidget.selectedItems()) > 0:
            index = self.ui.tableWidget.selectedItems()[0].row()
            self.user.user_data.delete_key(self.keys[index]['id'])
            self.close_key_editor()
            self.view_data()
        else:
            warning_notification("Не выбрана ни одна запись")

    def gen_pss(self):
        input_str = self.ui.stringEdit.text()
        if len(input_str) == 0:
            warning_notification("Пустая строка пароля!")
        else:
            model = self.ui.modelEdit.currentText()

            if model == 'Простой':
                pss = crypto.simple_alg(input_str)
            elif model == 'Сильный':
                pss = crypto.strong_alg(input_str)
            elif model == 'Случайный':
                pss = crypto.strong_alg(input_str)
            else:
                pss = input_str

            self.ui.password.setText(pss)

    def close_main_menu(self):
        self.ui.mainPage.setMaximumSize(0, 0)
        self.ui.settings.setMaximumSize(0, 0)
        self.ui.passwordManager.setMaximumSize(0, 0)

    def open_main_window(self, login):
        max = 16777215

        self.ui.username.setText(login)
        self.close_key_editor()
        self.close_main_menu()
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
            self.ui.sendCodeBtn.clicked.connect(self.send_code)
        else:
            self.ui.regBtn.setText("Сменить пароль")
            self.ui.sendCodeBtn.clicked.connect(self.send_reset_code)

        self.ui.codeInput.textChanged.connect(self.check_code)
        self.ui.regBtn.clicked.connect(self.registration)

    def send_code(self):
        email = self.ui.email.text()
        self.user.user_data.login = email
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

    def registration(self):
        mode = self.sender().text() == "Зарегистрироваться"
        if self.user.code_chck:
            status, msg = self.user.registration(self.ui.createPss.text(), self.ui.confPss.text(), mode)
            if status:
                self.ui.login.setText(str(self.user.user_data.login))
                self.open_login_window()
            else:
                warning_notification(msg)
        else:
            warning_notification('Почта не подтверждена')

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

    def close_general_windows(self):
        self.ui.mainPage.setMaximumSize(0, 0)
        self.ui.passwordManager.setMaximumSize(0, 0)
        self.ui.settings.setMaximumSize(0, 0)

    def view_data(self):
        col = self.col
        if col is not None:
            self.keys = self.user.user_data.get_all_docs()

            row = 0
            self.ui.tableWidget.setRowCount(len(self.keys))
            for key in self.keys:
                self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key['title']))
                self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(key['password']))
                row += 1

    def quit(self):
        write_current_user('', '')
        self.col = None
        self.user.user_data.login = ''
        self.current_id = None
        self.get_current_user()

    def download_data(self):
        data = self.user.user_data.get_all_docs()
        msg = "Список паролей:\n"

        for key in data:
            msg += f'Название: {key["title"]}, Пароль: {key["password"]}\n'

        self.user.mail.send_email(msg, "Выгрузка паролей", self.user.user_data.login)

    def delete_account(self):
        self.download_data()
        for key in self.keys:
            self.user.user_data.delete_key(key['id'])

        self.user.user_data.delete_user()
        self.quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyManager()
    window.show()

    sys.exit(app.exec())