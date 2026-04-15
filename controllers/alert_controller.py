from utils.logger_config import configurar_logger

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
NARANJA_REAL = "\033[38;5;208m"
RESET = "\033[0m" 

logger = configurar_logger()

class AlertController:
    def comprobar_alerta_temperatura(self, registro):
        alertas = []

        # Si la temperatura es mayor a 42 grados → alerta de color ...
        if registro["temperatura"] > 42:
            alertas.append(f"{ROJO}ALERTA ROJA: {RESET} Riesgo extremo por calor - Riesgo para la salud muy alto. {RESET}")
        elif registro["temperatura"] <= -10:
            alertas.append(f"{ROJO}ALERTA ROJA: {RESET} Frío extremo. Riesgo de heladas y nevadas severas. {RESET}")
        elif registro["temperatura"] >= 39:
            alertas.append(f"{NARANJA_REAL}ALERTA NARANJA: {RESET} Riesgo importante por calor - Se recomienda no salir en horas centrales del día. {RESET}")
        elif registro["temperatura"] <= -6:
            alertas.append(f"{NARANJA_REAL}ALERTA NARANJA: {RESET} Temperaturas gélidas. Riesgo de heladas y nevadas. Peligro en tuberías y la salud. {RESET}")
        elif registro["temperatura"] >= 36:
            alertas.append(f"{AMARILLO}ALERTA AMARILLA: {RESET} Riesgo por calor - Se recomienda no realizar actividades al aire libre. {RESET}")
        elif registro["temperatura"] <= -4:
            alertas.append(f"{AMARILLO}ALERTA AMARILLA: {RESET} Precaución por heladas. {RESET}")
        else:
            alertas.append(f"{VERDE}Nivel Verde{RESET} (Sin riesgo).{RESET}")


        if alertas:
            logger.warning(
                f"Alertas generadas: {alertas} para registro -> {registro}"
            )

        # Devolvemos la lista de alertas (puede estar vacía si no hay ninguna)
        return alertas
    
    
    def comprobar_alerta_viento(self, registro):
        alertas = []

        # Si el viento es mayor a 110km → alerta de color ...
        if registro["viento"] >= 110:
            alertas.append( f"{ROJO}ALERTA ROJA: Viento extremo - Peligro de caída de objetos y daños estructurales. {RESET}")
        elif registro["viento"] >= 90:
            alertas.append( f"{NARANJA_REAL}ALERTA NARANJA: Cierre preventivo de parques. {RESET}")
        elif registro["viento"] >= 70:
            alertas.append( f"{AMARILLO}ALERTA AMARILLA: Balizas en zonas infantiles y de mayores. {RESET}")
        else:
            alertas.append( f"{VERDE}Nivel Verde{RESET} (Sin riesgo).{RESET}")

        if alertas:
            logger.warning(
                f"Alertas generadas: {alertas} para registro -> {registro}"
            )

        return alertas