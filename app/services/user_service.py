"""
from domain.user import User
from domain.user_repository import UserRepositoryInterface

class UserService:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def register_user(self, username: str, password: str, email: str, role: str = "user") -> User:
        # Verificar si ya existe un usuario con ese email
        if self.user_repository.get_user_by_email(email):
            raise ValueError("Email already in use.")
        
        # Crear un nuevo usuario
        user = self.user_repository.create_user(username, password, email, role)
        return user

    def get_user_by_username(self, username: str) -> User:
        # Recuperar usuario por su nombre de usuario
        user = self.user_repository.get_user_by_username(username)
        if not user:
            raise ValueError("User not found.")
        return user
"""