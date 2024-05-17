import random
import libs.crypto as crypto
from libs.mail import Mail
from libs.connection import Data

users = 'accounts'


def is_login(_login):
    return '@' in _login and '.' in _login


class Account:
    def __init__(self):
        super(Account, self).__init__()
        self.mail = Mail()
        self.access = False
        self.code_chck = False
        self.code = None
        self.data = Data()

    def send_code(self, _login):
        if is_login(_login):
            check = False
            if self.data.get_user_with_login() is not None:
                check = True
            if not check:
                self.data.login = _login
                self.code = crypto.gen_code(4)
                status, msg = self.mail.send_email(f"Код подтверждения: {self.code}",
                                                   "Подтверждение почты", self.data.login)
                return status, msg
            else:
                return False, "Такой пользователь существует!"
        else:
            return False, 'Введен некорректный адрес электронной почты!'

    def send_reset_code(self, _login):
        self.data.login = _login
        if is_login(_login):
            check = False
            if self.data.get_user_with_login() is not None:
                check = True
            if check:
                self.code = crypto.gen_code(6)
                status, msg = self.mail.send_email(f"Код для сброса пароля: {self.code}",
                                                   "Сброс пароля", self.data.login)

                return status, msg
            else:
                return False, "Такой пользователь не существует!"
        else:
            return False, 'Введен некорректный адрес электронной почты!'

    def code_check(self, input_code, _login):
        if self.data.login == _login:
            if int(input_code) == self.code:
                self.code_chck = True
                return True, 'Код подтвержден'
            else:
                return False, 'Код не совпадает'
        else:
            return False, 'Почта была изменена'

    def registration(self, pss, conf_pss, create):
        email = self.data.login
        if len(pss) > 3:
            if pss == conf_pss:
                _data = {
                    'login': f"{email}",
                    'password': f"{pss}"
                }
                if create:
                    self.data.create_account(_data)
                    self.mail.send_email('Добро пожаловать в CryptoKey - менеджер генерации и хранения паролей\n'
                                         f'Ваш логин: {email}\nПароль: {pss}', "Вы в системе!", email)
                else:
                    user = self.data.get_user_with_login()
                    id = user['id']
                    self.data.update_pass(id, _data)

                return True, 'Done'
            else:
                return False, 'Пароли не совпадают'
        else:
            return False, 'Пароль должен быть от 4 символов'

    def login(self, _login, pss):
        self.data.login = _login
        acc_doc = self.data.get_user_with_login()
        self.access = False
        if acc_doc is not None:
            if acc_doc['password'] == pss:
                self.access = True

        return self.access
