import random
import sys
import os
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from libs.main_window_ui import Ui_MainWindow
from libs import login_ui, registration_ui, key_editor_ui
from libs.account import Account


translate1 = {
    'a': '@',
    'b': '6',
    'c': 'C',
    'd': 'd',
    'e': 'e',
    'f': '5',
    'g': 'g',
    'h': 'H',
    'i': '1',
    'j': 'j',
    'k': 'k',
    'l': 'L',
    'm': 'm',
    'n': 'N',
    'o': '0',
    'p': 'p',
    'q': 'Q',
    's': 'S',
    't': '2',
    'u': 'u',
    'v': 'V',
    'w': 'www',
    'x': 'X',
    'y': 'Y',
    'z': 'Z'
}

translate2 = {
    'a': 'A',
    'b': 'B',
    'c': 'c',
    'd': 'D',
    'e': '3',
    'f': 'F',
    'g': 'G',
    'h': 'h',
    'i': 'i',
    'j': 'J',
    'k': 'K',
    'l': 'l',
    'm': 'M',
    'n': 'n',
    'o': '_o_',
    'p': 'P',
    'q': 'q',
    's': 's',
    't': 'T',
    'u': 'u',
    'v': 'v',
    'w': 'W',
    'x': 'x',
    'y': 'y',
    'z': 'z'
}


def strong_alg(string):
    pss = string.lower()
    new_pss = ''
    for a in pss:
        if a in translate1 and a in translate2:
            if random.randint(0, 2) == 0:
                new_pss += translate1[a]
            else:
                new_pss += translate2[a]
        else:
            new_pss += a
            if random.randint(0, 5) >= 4:
                new_pss += '_'
    if len(new_pss) < 12:
        power = 11 - len(new_pss)
        new_pss += str(random.randint(10 ** power, 10 ** (power + 1) - 1))
    return new_pss


def simple_alg(string):
    power = random.randint(3, 8)
    return string + str(random.randint(10 ** power, 10 ** (power + 1) - 1))


def write_current_user(_login, pss):
    with open(f'{os.path.dirname(__file__)}\\data\\current_user', "w") as f:
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
        self.open_login_window()
        self.user = Account()
        self.get_current_user()

    def gen_pss(self):
        input_str = self.editor_window.stringEdit.text()
        if len(input_str) == 0:
            warning_notification("Пустая строка пароля!")
        else:
            model = self.editor_window.modelEdit.currentText()

            if model == 'Simple':
                pss = simple_alg(input_str)
            elif model == 'Strong':
                pss = strong_alg(input_str)
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
                    self.user.email = doc['login']
                    self.col = self.user.user_data.get_user_with_login(self.user.email)['collection']
                    self.open_main_window(doc['login'])
                else:
                    warning_notification('The password or username do not match!')

    def login(self):
        _login = self.login_window.login.text()
        pss = self.login_window.pss.text()
        if len(_login) == 0 or len(pss) == 0:
            warning_notification('An empty line!')
        else:
            if self.user.login(_login, pss):
                write_current_user(_login, pss)
                self.user.email = _login
                self.col = self.user.user_data.get_user_with_login(self.user.email)['collection']
                self.open_main_window(_login)
            else:
                warning_notification("The password or username do not match!")

    def open_registration_window(self):
        sender = self.sender()
        self.new_window = QtWidgets.QDialog()
        self.reg_window = registration_ui.Ui_dialog()

        if sender.text() == 'Sign up':
            self.reg_window.setupUi(self.new_window)

            self.reg_window.sendCodeBtn.clicked.connect(self.send_code)
        else:
            self.reg_window.setupUi(self.new_window)
            self.reg_window.label.setText("Reset password")
            self.reg_window.regBtn.setText("Сhange password")

            self.reg_window.sendCodeBtn.clicked.connect(self.send_reset_code)

        self.reg_window.checkCodeBtn.clicked.connect(self.check_code)
        self.reg_window.regBtn.clicked.connect(self.registration)
        self.new_window.show()

    def send_code(self):
        status, msg = self.user.send_code(self.reg_window.email.text())
        if not status:
            warning_notification(msg)
            self.login_window.login.setText(self.reg_window.email.text())
            self.new_window.close()

    def send_reset_code(self):
        status, msg = self.user.send_reset_code(self.reg_window.email.text())
        if not status:
            warning_notification(msg)
            self.login_window.login.setText(self.reg_window.email.text())

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
        mode = self.sender().text() == "Registration"

        if self.user.code_chck:
            status, msg = self.user.registration(self.reg_window.pss.text(), self.reg_window.confPss.text(), mode)
            if status:
                self.new_window.close()
                self.login_window.login.setText(str(self.user.email))
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
        self.ui_main.username.setText(user)

        self.view_data()

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

        if sender.text() == 'New Key':
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
            if self.editor_window.password.text() == "Password":
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
        data = {
            'password': f'{self.editor_window.password.text()}',
            'title': f'{self.editor_window.titleEdit.text()}',
            'collection': f'{self.col}'
        }
        self.user.user_data.update_existing_key(self.current_id, data)
        self.new_window.close()
        self.view_data()

    def delete_account(self):
        self.download_data()
        for key in self.keys:
            self.user.user_data.delete_key(key['id'])

        id = self.user.user_data.get_user_with_login(self.user.email)['id']
        self.user.user_data.delete_user(id, self.col)
        self.quit()

    def quit(self):
        write_current_user('', '')
        self.open_login_window()
        self.user.email = None
        self.col = None

    def view_data(self):
        col = self.col
        if col is not None:
            self.keys = self.user.user_data.get_all_docs(col)

            row = 0
            self.ui_main.tableWidget.setRowCount(len(self.keys))
            for key in self.keys:
                self.ui_main.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key['title']))
                self.ui_main.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(key['password']))
                row += 1

    def download_data(self):
        data = self.user.user_data.get_all_docs(self.col)
        msg = "Список паролей:\n"

        for key in data:
            msg += f'Название: {key["title"]}, Пароль: {key["password"]}\n'

        self.user.mail.send_email(msg, "Выгрузка паролей", self.user.email)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = KeyManager()
    window.show()

    sys.exit(app.exec())
