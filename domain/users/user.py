# domain/users/user.py
class User:
    def __init__(self, user_id, name, email, password):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f'{self.name} <{self.email}>'
