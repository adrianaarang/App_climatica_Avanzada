import json
import os
import re
import hashlib

class AuthManager:
    def __init__(self):
        # Configuramos la ruta al inicializar el objeto
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.data_path = os.path.join(self.base_dir, "usuarios.json")

    def encriptar_password(self, password):
        """Convierte el texto plano en un código SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def cargar_usuarios(self):
        """Lee los usuarios del archivo JSON."""
        if not os.path.exists(self.data_path):
            return []
        with open(self.data_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def guardar_usuarios(self, usuarios):
        """Guarda la lista de usuarios en el JSON."""
        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4)

    def registrar_usuario(self, email, password):
        """Lógica para registrar un nuevo usuario."""
        usuarios = self.cargar_usuarios()
        
        # Validación: ¿Ya existe el email?
        for u in usuarios:
            if u["username"] == email:
                return False, "El usuario ya existe."

        # Encriptamos y guardamos
        password_encriptada = self.encriptar_password(password)
        nuevo = {"username": email, "password": password_encriptada}

        usuarios.append(nuevo)
        self.guardar_usuarios(usuarios)
        return True, "Registro completado con éxito."

    def verificar_login(self, email, password):
        """Lógica para comprobar si el email y contraseña coinciden."""
        usuarios = self.cargar_usuarios()
        password_a_comprobar = self.encriptar_password(password)

        for u in usuarios:
            if u["username"] == email:
                if u["password"] == password_a_comprobar:
                    return True, "Login correcto."

        return False, "Email o contraseña incorrectos."

    def validar_datos(self, email, password):
        """Comprueba si el formato del email es correcto y la clave es larga."""
        # Expresión regular para validar email
        regex_email = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"

        if not re.match(regex_email, email):
            return False, "El formato del email no es válido."

        if len(password) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres."

        return True, "" 