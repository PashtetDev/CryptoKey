import random
import requests
from bs4 import BeautifulSoup
import libs.crypto as crypto
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os

collection = 'keysCollection'
users = 'accounts'


def convert_data(_data, _hash, flag):
    new_data = {}
    if flag:
        for key in _data:
            if key != 'protected_key' and key != 'login':
                new_data[key] = crypto.lock_key(_data[key], _hash)
            else:
                new_data[key] = _data[key]
    else:
        for key in _data:
            if key != 'protected_key' and key != 'login':
                new_data[key] = crypto.unlock_key(_data[key], _hash)
            else:
                new_data[key] = _data[key]
    return new_data


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.login = ''
        key_path = f'{os.path.dirname(__file__)}\\data\\firebase_key.json'
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def create_account(self, _data):
        _data['collection'] = f'col_{_data["login"]}_{random.randint(10 ** 4, 10 ** 5-1)}'
        _data['protected_key'] = crypto.gen_key(24)
        _hash = _data['protected_key']
        _data = convert_data(_data, _hash, True)
        doc_ref = self.db.collection(users).document()
        doc_ref.set(_data)

    def create_key(self, _data):
        _hash = self.get_user_with_login()['protected_key']

        _data = convert_data(_data, _hash, True)

        doc_ref = self.db.collection(collection).document()
        doc_ref.set(_data)

    def update_existing_key(self, doc_id, new_data):
        _hash = self.get_user_with_login()['protected_key']
        new_data = convert_data(new_data, _hash, True)

        collection_ref = self.db.collection(collection)
        doc_ref = collection_ref.document(doc_id)
        doc_ref.update(new_data)

    def update_pass(self, doc_id, new_data):
        _hash = self.get_user_with_login()['protected_key']
        new_data = convert_data(new_data, _hash, True)

        collection_ref = self.db.collection(users)
        doc_ref = collection_ref.document(doc_id)
        doc_ref.update(new_data)

    def get_all_docs(self):
        docs = (
            self.db.collection(collection).stream()
        )

        collection_name = self.get_user_with_login()['collection']
        _hash = self.get_user_with_login()['protected_key']

        documents_list = []
        for doc in docs:
            doc_data = doc.to_dict()
            if crypto.lock_key(collection_name, _hash) == doc_data['collection']:
                doc_data = convert_data(doc_data, _hash, False)
                doc_data['id'] = doc.id
                documents_list.append(doc_data)

        return documents_list

    def get_user_with_login(self):
        docs = (
            self.db.collection(users).stream()
        )
        for doc in docs:
            doc_data = doc.to_dict()
            if doc_data['login'] == self.login:
                _hash = doc_data['protected_key']
                doc_data = convert_data(doc_data, _hash, False)
                doc_data['id'] = doc.id
                return doc_data
        return None

    def delete_user(self):
        try:
            document_id = self.get_user_with_login()['id']
            doc_ref = self.db.collection(users).document(document_id)
            doc_ref.delete()
        except Exception as e:
            print(f"Error deleting document: {str(e)}")

    def delete_key(self, document_id):
        try:
            doc_ref = self.db.collection(collection).document(document_id)
            doc_ref.delete()
        except Exception as e:
            print(f"Error deleting document: {str(e)}")

    def reliability_check(self):
        docs = self.get_all_docs()
        reliability = {}
        for doc in docs:
            reliability[doc['password']] = {}
            reliability[doc['password']]['number_flag'] = False
            reliability[doc['password']]['upper_flag'] = False
            reliability[doc['password']]['lower_flag'] = False
            reliability[doc['password']]['special_flag'] = False
            reliability[doc['password']]['length'] = len(doc['password'])
            for c in doc['password']:
                if 48 <= ord(c) <= 57:
                    reliability[doc['password']]['number_flag'] = True
                elif 65 <= ord(c) <= 90:
                    reliability[doc['password']]['upper_flag'] = True
                elif 97 <= ord(c) <= 122:
                    reliability[doc['password']]['lower_flag'] = True
                else:
                    reliability[doc['password']]['special_flag'] = True
            reliability[doc['password']]['time'] = self.get_time(reliability[doc['password']]['number_flag'],
                                                                 reliability[doc['password']]['lower_flag'],
                                                                 reliability[doc['password']]['upper_flag'],
                                                                 reliability[doc['password']]['special_flag'],
                                                                 reliability[doc['password']]['length'])

        return reliability

    def get_time(self, number, lower, upper, special, length):
        time = ''
        if length < 7:
            time = 'Мгновенно'
            comment = 'Пароль требует увеличения длины!'
        elif length == 7:
            if number and lower and upper and special:
                time = '31 секунда'
            elif number and lower and upper:
                time = '7 сек'
            elif lower and upper:
                time = '2 сек'
            elif lower:
                time = 'Мгновенное'
            else:
                time = 'Мгновенное'
        elif length == 8:
            if number and lower and upper and special:
                time = '39 минут'
            elif number and lower and upper:
                time = '7 минут'
            elif lower and upper:
                time = '2 минуты'
            elif lower:
                time = 'Мгновенное'
            else:
                time = 'Мгновенное'
        elif length == 9:
            if number and lower and upper and special:
                time = '2 дня'
            elif number and lower and upper:
                time = '7 часов'
            elif lower and upper:
                time = '1 час'
            elif lower:
                time = '10 секунд'
            else:
                time = 'Мгновенное'
        elif length == 10:
            if number and lower and upper and special:
                time = '5 месяцев'
            elif number and lower and upper:
                time = '3 недели'
            elif lower and upper:
                time = '3 дня'
            elif lower:
                time = '4 минуты'
            else:
                time = 'Мгновенно'
        elif length == 11:
            if number and lower and upper and special:
                time = '34 года'
            elif number and lower and upper:
                time = '3 года'
            elif lower and upper:
                time = '5 месяцев'
            elif lower:
                time = '2 часа'
            else:
                time = 'Мгновенное'
        elif length == 12:
            if number and lower and upper and special:
                time = '3000 лет'
            elif number and lower and upper:
                time = '200 лет'
            elif lower and upper:
                time = '24 года'
            elif lower:
                time = '2 дня'
            else:
                time = '2 сек'
        elif length == 13:
            if number and lower and upper and special:
                time = '202 тысячи лет'
            elif number and lower and upper:
                time = '12 тысяч лет'
            elif lower and upper:
                time = '1 000 лет'
            elif lower:
                time = '2 месяца'
            else:
                time = '19 секунд'
        elif length == 14:
            if number and lower and upper and special:
                time = '16 миллионов лет'
            elif number and lower and upper:
                time = '750 тысяч лет'
            elif lower and upper:
                time = '64 тысячи лет'
            elif lower:
                time = '4 года'
            else:
                time = '3 минуты'
        elif length == 15:
            if number and lower and upper and special:
                time = '1 миллиард лет'
            elif number and lower and upper:
                time = '46 миллионов лет'
            elif lower and upper:
                time = '3 миллиона лет'
            elif lower:
                time = '100 лет'
            else:
                time = '32 минуты'
        elif length == 16:
            if number and lower and upper and special:
                time = '92 миллиарда лет'
            elif number and lower and upper:
                time = '3 миллиарда лет'
            elif lower and upper:
                time = '173 миллиона лет'
            elif lower:
                time = '3000 лет'
            else:
                time = '5 часов'
        elif length == 17:
            if number and lower and upper and special:
                time = '7 триллионов лет'
            elif number and lower and upper:
                time = '179 миллиардов лет'
            elif lower and upper:
                time = '9 миллиардов лет'
            elif lower:
                time = '69 тысяч лет'
            else:
                time = '2 дня'
        else:
            if number and lower and upper and special:
                time = '438 триллионов лет'
            elif number and lower and upper:
                time = '11 триллионов лет'
            elif lower and upper:
                time = '467 миллионов лет'
            elif lower:
                time = '2 миллиона лет'
            else:
                time = '3 недели'
        return time

    def get_last_news(self):
        req = requests.get("https://habr.com/ru/hubs/infosecurity/articles/")
        src = req.text
        soup = BeautifulSoup(src, 'lxml')

        filtered_news = []
        filtered_links = []
        filtered_authors = []
        all_news = soup.findAll('article', class_='tm-articles-list__item')
        for data_ in all_news:
            if data_.find('a', class_='tm-title__link') is not None:
                filtered_news.append(data_.find('a', class_='tm-title__link').text)
                filtered_links.append(f'https://habr.com{data_.find("a", class_="tm-title__link")["href"]}')
                filtered_authors.append(data_.find('a', class_='tm-user-info__username').text)

        return filtered_news, filtered_links, filtered_authors
