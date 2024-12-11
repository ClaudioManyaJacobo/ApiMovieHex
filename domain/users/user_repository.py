# domain/users/user_repository.py
from abc import ABC, abstractmethod
from domain.users.user import User

# Interfaz que define los métodos que debe implementar un repositorio de usuarios
class UserRepository(ABC):
    # Método para obtener un usuario por su ID
    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass
    
    # Método para obtener un usuario por su email
    @abstractmethod
    def create_user(self, user: User) -> User:
        pass
    
# metodos que aun no estan implementados   
    # Método para actualizar un usuario
    @abstractmethod
    def update_user(self, user: User) -> User:
        pass
    
    # Método para eliminar un usuario
    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        pass
# ***********************************************