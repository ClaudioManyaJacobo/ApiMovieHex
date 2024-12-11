import bcrypt
from domain.users.user_repository import UserRepository
from domain.users.user import User

# Clase para representar un servicio de usuarios
class UserService:
    # Servicio para manejar la lógica de negocio relacionada con los usuarios.
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    # Método para hashear una contraseña
    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # Método para verificar una contraseña
    def verify_password(self, password: str, hashed_password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

    # Método para crear un usuario
    def create_user(self, name: str, email: str, password: str) -> User:
        hashed_password = self.hash_password(password)
        user = User(user_id=None, name=name, email=email, password=hashed_password)
        return self.user_repository.create_user(user)

    # Método para validar un usuario
    def validate_user(self, email: str, password: str) -> User:
        user = self.user_repository.get_user_by_email(email)
        if user and self.verify_password(password, user.password):
            return user
        return None

# **********************************************************
    # Método para obtener un usuario por su email
    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_user_by_email(email)

    # Método para obtener un usuario por su ID
    def get_user(self, user_id: int) -> User:
        return self.user_repository.get_user_details(user_id)