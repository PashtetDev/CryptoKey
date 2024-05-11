import random
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
        _data['protected_key'] = crypto.gen_key(12)
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

