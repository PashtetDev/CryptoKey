import random
from mail import Mail
from connection import Data


users = 'accounts'


def gen_code(len):
    return random.randint(10 ** len, 10 ** (len + 1) - 1)


def is_login(_login):
    return '@' in _login and '.' in _login


class Account:
    def __init__(self):
        super(Account, self).__init__()
        self.user_data = Data()
        self.mail = Mail()
        self.access = False
        self.code_chck = False
        self.email = None
        self.code = None

    def send_code(self, _login):
        if is_login(_login):
            check = False
            if self.user_data.get_user_with_login(_login) is not None:
                check = True
            if not check:
                self.email = _login
                self.code = gen_code(4)
                print(self.code)
                self.mail.send_email(f"Код подтверждения: {self.code}", "Подтверждение почты", self.email)
                return True, 'Код отправлен'
            else:
                return False, "Такой пользователь существует!"
        else:
            return False, 'Введен некорректный адрес электронной почты!'

    def send_reset_code(self, _login):
        if is_login(_login):
            check = False
            if self.user_data.get_user_with_login(_login) is not None:
                check = True
            if check:
                self.email = _login
                self.code = gen_code(6)
                print(self.code)
                self.mail.send_email(f"Код для сброса пароля: {self.code}", "Сброс пароля", self.email)
                return True, 'Код отправлен'
            else:
                return False, "Такой пользователь не существует!"
        else:
            return False, 'Введен некорректный адрес электронной почты!'

    def code_check(self, input_code, _login):
        if self.email == _login:
            if int(input_code) == self.code:
                self.code_chck = True
                return True, 'Код подтвержден'
            else:
                return False, 'Код не совпадает'
        else:
            return False, 'Почта была изменена'

    def registration(self, pss, conf_pss, create):
        if len(pss) > 3:
            if pss == conf_pss:
                _data = {
                    'login': f"{self.email}",
                    'password': f"{pss}"
                }
                if create:
                    self.user_data.create_account(_data)
                    self.mail.send_email('Добро пожаловать в CryptoKey - менеджер генерации и хранения паролей\n'
                                         f'Ваш логин: {self.email}\nПароль: {pss}', "Вы в системе!", self.email)
                else:
                    user = self.user_data.get_user_with_login(self.email)
                    print(user)
                    id = user['id']
                    self.user_data.update_pass(id, _data)
                    self.mail.send_email('Ваш пароль был изменен.\n'
                                         f'Ваш логин: {self.email}\nПароль: {pss}', "Смена пароля", self.email)

                return True, 'Done'
            else:
                return False, 'Пароли не совпадают'
        else:
            return False, 'Пароль должен быть от 4 символов'

    def login(self, _login, pss):
        acc_doc = self.user_data.get_user_with_login(_login)

        if acc_doc is not None:
            if acc_doc['password'] == pss:
                self.access = True

        return self.access

    def send_pass(self):
        log_doc = self.user_data.get_document_with_login(users, self.email)
        if is_login(self.email) and log_doc is not None:
            self.mail.send_email(f"Выш пароль: {log_doc['password']}", "Выгрузка паролей", self.email)
        else:
            print('Данный пользователь не найден')
