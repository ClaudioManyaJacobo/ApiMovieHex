# infrastructure/user_db/sqlite_user_repository.py
import sqlite3
from domain.users.user import User
from domain.users.user_repository import UserRepository

# Clase para representar un repositorio de usuarios en SQLite
class SQLiteUserRepository(UserRepository):
    # Inicializamos la conexión a la base de datos
    def __init__(self, database_path: str):
        self.connection = sqlite3.connect(database_path, check_same_thread=False)
        self._initialize_db()

    # Método para inicializar la base de datos
    def _initialize_db(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            ''')
            
    # Método para obtener un usuario por su email
    def get_user_by_email(self, email: str) -> User:
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, name, email, password FROM users WHERE email = ?", (email,))
            row = cursor.fetchone()
            if row:
                return User(user_id=row[0], name=row[1], email=row[2], password=row[3])
        finally:
            cursor.close()
        return None

    # Método para crear un usuario
    def create_user(self, user: User) -> User:
        try:
            with self.connection:
                cursor = self.connection.cursor()
                cursor.execute(
                    "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                    (user.name, user.email, user.password)
                )
            return user
        except sqlite3.IntegrityError:
            raise ValueError("El correo electrónico ya está en uso.")

# METODOS QUE AUN NO ESTAN IMPLEMENTADOS
    # Método para actualizar un usuario
    def update_user(self, user: User) -> User:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (user.name, user.email, user.id))
        return user

    # Método para eliminar un usuario
    def delete_user(self, user_id: int) -> bool:
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            return cursor.rowcount > 0
# ****************************************************
    # Método para cerrar la conexión a la base de datos
    def close(self):
        if self.connection:
            self.connection.close()
