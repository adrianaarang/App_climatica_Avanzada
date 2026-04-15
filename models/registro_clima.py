class RegistroClima:
    """
    Esta clase representa un registro meteorológico.

    Cada objeto de esta clase contiene todos los datos
    introducidos por el usuario sobre el clima.
    """

    def __init__(self, fecha, zona, temperatura, humedad, viento, lluvia, alertas=None):
        """
        Constructor de la clase.

        Parámetros:
        - fecha: fecha del registro
        - zona: ubicación (comunidad autónoma)
        - temperatura: temperatura en grados
        - humedad: porcentaje de humedad
        - viento: velocidad del viento
        - lluvia: cantidad de lluvia
        - alertas: lista de alertas (opcional)
        """

        # Asignamos cada valor a un atributo del objeto
        self.fecha = fecha
        self.zona = zona
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        self.lluvia = lluvia

        # Si no se pasan alertas, se inicializa como lista vacía
        # Esto evita errores y asegura que siempre sea una lista
        self.alertas = alertas if alertas is not None else []

    def to_dict(self):
        """
        Convierte el objeto en un diccionario.

        Esto es necesario porque los archivos JSON solo pueden guardar
        datos en formato diccionario (no objetos de Python).
        """

        return {
            "fecha": self.fecha,
            "zona": self.zona,
            "temperatura": self.temperatura,
            "humedad": self.humedad,
            "viento": self.viento,
            "lluvia": self.lluvia,
            "alertas": self.alertas
        }