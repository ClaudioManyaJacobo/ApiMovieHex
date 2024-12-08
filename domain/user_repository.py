"""
from abc import ABC, abstractmethod
from typing import Optional
from domain.user import User

# Interfaz para el repositorio de usuarios
class UserRepositoryInterface(ABC):
    # Método para obtener un usuario por su ID
    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass
    
    # Método para obtener un usuario por su nombre de usuario
    @abstractmethod
    def get_user_by_username(self, username: str) -> Optional[User]:
        pass

    # Método para obtener un usuario por su correo electrónico
    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        pass
    
    # Método para obtener todos los usuarios
    @abstractmethod
    def create_user(self, username: str, password: str, email: str, role: str) -> User:
        pass

    # Método para actualizar la información de un usuario
    @abstractmethod
    def update_user(self, user: User) -> None:
        pass
    
    # Método para eliminar un usuario por su ID
    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass      
"""