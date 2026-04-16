from utils.logger_config import configurar_logger

# En Flask mostramos las alertas en HTML, no en consola.
# Por eso usamos etiquetas span con clases CSS en vez de códigos ANSI.
ROJO = '<span class="alerta-roja">'
VERDE = '<span class="alerta-verde">'
AMARILLO = '<span class="alerta-amarilla">'
NARANJA_REAL = '<span class="alerta-naranja">'
RESET = '</span>'

logger = configurar_logger()


class AlertController:
    def comprobar_alertas(self, registro):
        alertas = []

        alertas.extend(self.comprobar_alerta_temperatura(registro))
        alertas.extend(self.comprobar_alerta_viento(registro))

        alertas_reales = [alerta for alerta in alertas if "Nivel Verde" not in alerta]

        if not alertas_reales:
            return [f"{VERDE}Nivel Verde:{RESET} Sin riesgo."]

        return alertas_reales

    def comprobar_alerta_temperatura(self, registro):
        alertas = []

        temperatura = float(registro["temperatura"])

        if temperatura > 42:
            alertas.append(
                f"{ROJO}ALERTA ROJA:{RESET} Riesgo extremo por calor - Riesgo para la salud muy alto."
            )
        elif temperatura <= -10:
            alertas.append(
                f"{ROJO}ALERTA ROJA:{RESET} Frío extremo. Riesgo de heladas y nevadas severas."
            )
        elif temperatura >= 39:
            alertas.append(
                f"{NARANJA_REAL}ALERTA NARANJA:{RESET} Riesgo importante por calor - Evitar salir en horas centrales."
            )
        elif temperatura <= -6:
            alertas.append(
                f"{NARANJA_REAL}ALERTA NARANJA:{RESET} Temperaturas gélidas. Riesgo de heladas."
            )
        elif temperatura >= 36:
            alertas.append(
                f"{AMARILLO}ALERTA AMARILLA:{RESET} Riesgo por calor."
            )
        elif temperatura <= -4:
            alertas.append(
                f"{AMARILLO}ALERTA AMARILLA:{RESET} Precaución por heladas."
            )

        if alertas:
            logger.warning(
                f"Alertas de temperatura generadas: {alertas} para registro -> {registro}"
            )

        return alertas

    def comprobar_alerta_viento(self, registro):
        alertas = []

        viento = float(registro["viento"])

        if viento >= 110:
            alertas.append(
                f"{ROJO}ALERTA ROJA:{RESET} Viento extremo - Daños estructurales."
            )
        elif viento >= 90:
            alertas.append(
                f"{NARANJA_REAL}ALERTA NARANJA:{RESET} Cierre de parques."
            )
        elif viento >= 70:
            alertas.append(
                f"{AMARILLO}ALERTA AMARILLA:{RESET} Precaución en exteriores."
            )

        if alertas:
            logger.warning(
                f"Alertas de viento generadas: {alertas} para registro -> {registro}"
            )

        return alertas