from common.database import Database

class User(object):
    def __init__(self,account, password):
        self.account = account
        self.password = password
        self.database = Database('localhost:27017','user')

    def is_login_valid(self):
        user_data = self.database.find_one(collection='users',data={'account':self.account})
        print(user_data)
        if user_data is None:
            return False
        elif user_data['password'] != self.password:
            return False
        else:
            return True

    def register_user(self,account):
        result = self.database.find_one(collection='users',data={'account':account})
        if result is not None:
            return False
        else:
            self.save_to_db()
            return True



    def save_to_db(self):
        self.database.insert(collection='users',data=self.json())

    def json(self):
        return {
            "account": self.account,
            "password": self.password,

        }
    def find_user_data(self,account):
        return self.database.find_one(collection='users',data={'account':account})
