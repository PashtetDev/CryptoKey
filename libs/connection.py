import random
import libs.crypto as crypto
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.collection = 'keysCollection'
        self.users = 'accounts'

        key_path = f'{os.path.dirname(__file__)}\\data\\firebase_key.json'
        cred = credentials.Certificate(key_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def create_account(self, _data):
        _data['collection'] = f'col_{_data["login"]}_{random.randint(10 ** 4, 10 ** 5-1)}'
        _data['protected_key'] = crypto.gen_key(12)
        _data['password'] = crypto.lock_key(_data['password'], _data['protected_key'])
        doc_ref = self.db.collection(self.users).document()
        doc_ref.set(_data)

    def create_key(self, _data, login):
        _hash = self.get_user_with_login(login)['protected_key']
        _data['password'] = crypto.lock_key(_data['password'], _hash)
        doc_ref = self.db.collection(self.collection).document()
        doc_ref.set(_data)

    def update_existing_key(self, doc_id, new_data):
        collection_ref = self.db.collection(self.collection)
        doc_ref = collection_ref.document(doc_id)
        doc_ref.update(new_data)

    def update_pass(self, doc_id, new_data):
        collection_ref = self.db.collection(self.users)
        doc_ref = collection_ref.document(doc_id)
        doc_ref.update(new_data)

    def get_all_docs(self, collection_name):
        docs = (
            self.db.collection(self.collection).stream()
        )

        login = collection_name.split('_')[1]
        _hash = self.get_user_with_login(login)['protected_key']

        documents_list = []
        for doc in docs:
            doc_data = doc.to_dict()
            if doc_data['collection'] == collection_name:
                doc_data['id'] = doc.id
                doc_data['password'] = crypto.unlock_key(doc_data['password'], _hash)
                documents_list.append(doc_data)

        return documents_list

    def get_user_with_login(self, login):
        docs = (
            self.db.collection(self.users).stream()
        )
        for doc in docs:
            doc_data = doc.to_dict()
            doc_data['id'] = doc.id
            if doc_data['login'] == login:
                _hash = doc_data['protected_key']
                doc_data['password'] = crypto.unlock_key(doc_data['password'], _hash)
                return doc_data
        return None

    def delete_user(self, document_id, col):
        try:
            doc_ref = self.db.collection(self.users).document(document_id)
            doc_ref.delete()
        except Exception as e:
            print(f"Error deleting document: {str(e)}")

    def delete_key(self, document_id):
        try:
            doc_ref = self.db.collection(self.collection).document(document_id)
            doc_ref.delete()
        except Exception as e:
            print(f"Error deleting document: {str(e)}")
