import smtplib
import os
from email.mime.text import MIMEText


class Mail:
    def __init__(self):
        super(Mail, self).__init__()
        self.sender = 'crypto.key.service@gmail.com'
        with open(f'{os.path.dirname(__file__)}\\data\\pass', "r") as f:
            self.password = f.read()

    def send_email(self, message, theme, recipient):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        try:
            server.login(self.sender, self.password)
            _msg = MIMEText(f'{message}')
            _msg['Subject'] = theme
            server.sendmail(self.sender, recipient, _msg.as_string())
            server.quit()
            return True, 'Код отправлен'
        except Exception:
            print(str(Exception))
            return False, 'Что-то пошло не так. Проверьте почту'
