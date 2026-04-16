import sys
import os
import pytest


from controllers.alert_controller import AlertController

# 3. CONSTANTES HTML (Exactamente como están en tu AlertController)
ROJO = '<span class="alerta-roja">'
VERDE = '<span class="alerta-verde">'
AMARILLO = '<span class="alerta-amarilla">'
NARANJA_REAL = '<span class="alerta-naranja">'
RESET = '</span>'

@pytest.fixture
def ac():
    """Prepara una instancia del controlador antes de cada test"""
    return AlertController()

# --- TESTS DE TEMPERATURA ---

def test_alerta_temperatura(ac):
    assert ac.comprobar_alerta_temperatura({"temperatura": 45})[0] == f"{ROJO}ALERTA ROJA:{RESET} Riesgo extremo por calor - Riesgo para la salud muy alto."
    assert ac.comprobar_alerta_temperatura({"temperatura": -10})[0] == f"{ROJO}ALERTA ROJA:{RESET} Frío extremo. Riesgo de heladas y nevadas severas."
    assert ac.comprobar_alerta_temperatura({"temperatura": 39})[0] == f"{NARANJA_REAL}ALERTA NARANJA:{RESET} Riesgo importante por calor - Evitar salir en horas centrales."
    assert ac.comprobar_alerta_temperatura({"temperatura": -6})[0] == f"{NARANJA_REAL}ALERTA NARANJA:{RESET} Temperaturas gélidas. Riesgo de heladas."
    assert ac.comprobar_alerta_temperatura({"temperatura": 36})[0] == f"{AMARILLO}ALERTA AMARILLA:{RESET} Riesgo por calor."
    assert ac.comprobar_alerta_temperatura({"temperatura": -4})[0] == f"{AMARILLO}ALERTA AMARILLA:{RESET} Precaución por heladas."
    

# --- TESTS DE VIENTO ---

def test_alerta_viento(ac):
    assert ac.comprobar_alerta_viento({"viento": 120})[0] == f"{ROJO}ALERTA ROJA:{RESET} Viento extremo - Daños estructurales."
    assert ac.comprobar_alerta_viento({"viento": 100})[0] == f"{NARANJA_REAL}ALERTA NARANJA:{RESET} Cierre de parques."
    assert ac.comprobar_alerta_viento({"viento": 80})[0] == f"{AMARILLO}ALERTA AMARILLA:{RESET} Precaución en exteriores."

# --- TEST DE INTEGRACIÓN (Ambas alertas) ---

def test_multiples_alertas(ac):
    registro = {"temperatura": 50, "viento": 120}
    resultado = ac.comprobar_alertas(registro)
    # Debería haber 2 alertas en la lista, 
    assert len(resultado) == 2 # 
    assert "calor" in resultado[0]
    assert "Viento" in resultado[1]

def test_nivel_verde_cuando_todo_ok(ac):
    registro = {"temperatura": 25, "viento": 10}
    resultado = ac.comprobar_alertas(registro)
    esperado = f"{VERDE}Nivel Verde:{RESET} Sin riesgo."
    assert resultado[0] == esperado