"""
# domain/user.py
# Clase para representar un usuario
class User:
    def __init__(self, user_id, username, password, email,  role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        
    def __repr__(self):
        return f"<User {self.username}>"
    
"""