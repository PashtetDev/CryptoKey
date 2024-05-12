import random
import sys
import os
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from libs.main_window_ui import Ui_MainWindow
from libs import login_ui, registration_ui, key_editor_ui, crypto
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
        super(KeyManager, self).__init__()
        self.col = None
        self.current_id = None
        self.user = Account()
        self.get_current_user()

    def gen_pss(self):
        input_str = self.editor_window.stringEdit.text()
        if len(input_str) == 0:
            warning_notification("Пустая строка пароля!")
        else:
            model = self.editor_window.modelEdit.currentText()

            if model == 'Простой':
                pss = crypto.simple_alg(input_str)
            elif model == 'Сильный':
                pss = crypto.strong_alg(input_str)
            else:
                pss = input_str

            self.editor_window.password.setText(pss)

    def open_login_window(self):
        self.login_window = login_ui.Ui_MainWindow()
        self.login_window.setupUi(self)
        self.login_window.loginBtn.clicked.connect(self.login)
        self.login_window.signupBtn.clicked.connect(self.open_registration_window)
        self.login_window.resetPassBtn.clicked.connect(self.open_registration_window)

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
        _login = self.login_window.login.text()
        pss = self.login_window.pss.text()
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

    def open_registration_window(self):
        sender = self.sender()
        self.new_window = QtWidgets.QDialog()
        self.reg_window = registration_ui.Ui_dialog()

        if sender.text() == 'Регистрация':
            self.reg_window.setupUi(self.new_window)

            self.reg_window.sendCodeBtn.clicked.connect(self.send_code)
        else:
            self.reg_window.setupUi(self.new_window)
            self.reg_window.label.setText("Сброс пароля")
            self.reg_window.regBtn.setText("Сменить пароль")
            self.reg_window.sendCodeBtn.clicked.connect(self.send_reset_code)

        self.reg_window.checkCodeBtn.clicked.connect(self.check_code)
        self.reg_window.regBtn.clicked.connect(self.registration)
        self.new_window.show()

    def send_code(self):
        email = self.reg_window.email.text()
        self.user.user_data.login = email
        status, msg = self.user.send_code(email)
        if not status:
            warning_notification(msg)
            self.login_window.login.setText(email)
            self.new_window.close()

    def send_reset_code(self):
        email = self.reg_window.email.text()
        status, msg = self.user.send_reset_code(email)
        if not status:
            warning_notification(msg)
            self.login_window.login.setText(email)

    def check_code(self):
        status, msg = self.user.code_check(self.reg_window.codeInput.text(), self.reg_window.email.text())
        if not status:
            warning_notification(msg)
        else:
            self.reg_window.emailCheck.setCheckable(True)
            self.reg_window.emailCheck.setChecked(True)
            self.reg_window.email.setReadOnly(True)
            self.reg_window.codeInput.setReadOnly(True)

    def registration(self):
        mode = self.sender().text() == "Зарегистрироваться"
        if self.user.code_chck:
            status, msg = self.user.registration(self.reg_window.pss.text(), self.reg_window.confPss.text(), mode)
            if status:
                self.new_window.close()
                self.login_window.login.setText(str(self.user.user_data.login))
            else:
                warning_notification(msg)
        else:
            warning_notification('Почта не подтверждена')

    def open_main_window(self, user):
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        self.ui_main.newKeyBtn.clicked.connect(self.open_key_editor)
        self.ui_main.editBtn.clicked.connect(self.open_key_editor)
        self.ui_main.deleteBtn.clicked.connect(self.delete_current_key)
        self.ui_main.delAccButton.clicked.connect(self.delete_account)
        self.ui_main.quitBtn.clicked.connect(self.quit)
        self.ui_main.uploadBtn.clicked.connect(self.download_data)
        self.ui_main.tableWidget.clicked.connect(self.write_selected_pss)
        self.ui_main.username.setText(user)

        self.view_data()

    def write_selected_pss(self):
        if len(self.ui_main.tableWidget.selectedItems()) > 0:
            index = self.ui_main.tableWidget.selectedItems()[0].row()
            self.ui_main.selectedPss.setText(self.keys[index]['password'])
        else:
            self.ui_main.selectedPss.setText("")

    def delete_current_key(self):
        if len(self.ui_main.tableWidget.selectedItems()) > 0:
            index = self.ui_main.tableWidget.selectedItems()[0].row()
            self.user.user_data.delete_key(self.keys[index]['id'])
            self.view_data()
        else:
            warning_notification("Не выбрана ни одна запись")

    def open_key_editor(self):
        sender = self.sender()
        self.new_window = QtWidgets.QDialog()
        self.editor_window = key_editor_ui.Ui_dialog()
        self.editor_window.setupUi(self.new_window)
        self.editor_window.generateBtn.clicked.connect(self.gen_pss)

        if sender.text() == 'Новый пароль':
            self.editor_window.saveBtn.clicked.connect(self.add_key)
            self.new_window.show()
        else:
            self.editor_window.saveBtn.clicked.connect(self.update_key)
            if len(self.ui_main.tableWidget.selectedItems()) > 0:
                index = self.ui_main.tableWidget.selectedItems()[0].row()
                self.current_id = self.keys[index]['id']
                self.editor_window.password.setText(self.keys[index]['password'])
                self.editor_window.titleEdit.setText(self.keys[index]['title'])
                self.new_window.show()
            else:
                warning_notification("Не выбрана ни одна запись")

    def add_key(self):
        if len(self.editor_window.stringEdit.text()) == 0 or len(self.editor_window.titleEdit.text()) == 0:
            warning_notification("Обнаружены пустые строки!")
        else:
            if self.editor_window.password.text() == "Пароль":
                warning_notification("Сгенерируйте пароль!")
            else:
                data = {
                    'password': f'{self.editor_window.password.text()}',
                    'title': f'{self.editor_window.titleEdit.text()}',
                    'collection': f'{self.col}'
                }
                self.user.user_data.create_key(data)
                self.new_window.close()
                self.view_data()

    def update_key(self):
        new_data = {
            'password': f'{self.editor_window.password.text()}',
            'title': f'{self.editor_window.titleEdit.text()}',
            'collection': f'{self.col}'
        }
        self.user.user_data.update_existing_key(self.current_id, new_data)
        self.new_window.close()
        self.view_data()

    def delete_account(self):
        self.download_data()
        for key in self.keys:
            self.user.user_data.delete_key(key['id'])

        self.user.user_data.delete_user()
        self.quit()

    def quit(self):
        write_current_user('', '')
        self.col = None
        self.user.user_data.login = ''
        self.current_id = None
        self.get_current_user()

    def view_data(self):
        col = self.col
        if col is not None:
            self.keys = self.user.user_data.get_all_docs()

            row = 0
            self.ui_main.tableWidget.setRowCount(len(self.keys))
            for key in self.keys:
                self.ui_main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key['title']))
                self.ui_main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(key['password']))
                row += 1

    def download_data(self):
        data = self.user.user_data.get_all_docs()
        msg = "Список паролей:\n"

        for key in data:
            msg += f'Название: {key["title"]}, Пароль: {key["password"]}\n'

        self.user.mail.send_email(msg, "Выгрузка паролей", self.user.user_data.login)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyManager()
    window.show()

    sys.exit(app.exec())
