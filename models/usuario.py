class Usuario:
    """
    Esta clase representa un usuario del sistema.

    Contiene la información básica necesaria para autenticarse:
    - email
    - contraseña
    """

    def __init__(self, email, password):
        """
        Constructor de la clase.

        Parámetros:
        - email: correo electrónico del usuario
        - password: contraseña del usuario
        """

        # Guardamos los datos como atributos del objeto
        self.email = email
        self.password = password

    def to_dict(self):
        """
        Convierte el objeto Usuario en un diccionario.

        Esto es necesario porque los datos se guardan en un archivo JSON,
        y JSON solo admite diccionarios, no objetos de Python.
        """

        return {
            "email": self.email,
            "password": self.password
        }