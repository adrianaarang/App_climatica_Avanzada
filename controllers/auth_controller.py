import json
import os
import re
import hashlib

class AuthController:
    def __init__(self):
        # --- CÓDIGO VIEJO (Se guardaba en la misma carpeta del controlador) ---
        # self.base_dir = os.path.dirname(os.path.abspath(__file__))
        # self.data_path = os.path.join(self.base_dir, "usuarios.json")
        
        # --- CÓDIGO NUEVO ---
        # Subimos un nivel para que la carpeta 'data' esté en la raíz del proyecto, no dentro de 'controllers'.
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.data_dir = os.path.join(self.base_dir, "data")
        self.data_path = os.path.join(self.data_dir, "usuarios.json")

        # Aseguramos que la carpeta exista para evitar errores de "Ruta no encontrada"
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def encriptar_password(self, password):
        """Convierte el texto plano en un código SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def cargar_usuarios(self):
        """Lee los usuarios del archivo JSON."""
        if not os.path.exists(self.data_path):
            return []
        try:
            with open(self.data_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def guardar_usuarios(self, usuarios):
        """Guarda la lista de usuarios en el JSON dentro de la carpeta data."""
        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)

    def registrar_usuario(self, email, password):
        """Lógica para registrar un nuevo usuario."""
        valido, msg = self.validar_datos(email, password)
        if not valido:
            return False, msg

        usuarios = self.cargar_usuarios()
        
        for u in usuarios:
            if u["username"] == email:
                return False, "El usuario ya existe."

        password_encriptada = self.encriptar_password(password)
        nuevo = {"username": email, "password": password_encriptada}

        usuarios.append(nuevo)
        self.guardar_usuarios(usuarios)
        return True, "Registro completado con éxito."

    # --- CÓDIGO VIEJO (Nombre no coincidente con app.py) ---
    # def verificar_login(self, email, password):
    
    # --- CÓDIGO NUEVO ---
    # Se renombra a 'iniciar_sesion' porque app.py busca exactamente ese nombre.
    def iniciar_sesion(self, email, password):
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
        # --- CÓDIGO VIEJO (Regex muy restrictiva) ---
        # regex_email = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"
        
        # --- CÓDIGO NUEVO ---
        # Regex estándar que acepta mayúsculas, puntos y dominios modernos (ej. .technology, .es).
        regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(regex_email, email):
            return False, "El formato del email no es válido."

        if len(password) < 6:
            return False, "La contraseña debe tener al menos 6 caracteres."

        return True, ""