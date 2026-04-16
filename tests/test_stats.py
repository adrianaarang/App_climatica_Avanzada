import pytest
import pandas as pd
# Importamos la función directamente
from utils.stats import calcular_estadisticas

def test_estadisticas_basicas():
    # 1. PREPARAMOS DATOS DE PRUEBA (Mock data)
    datos = [
        {"zona": "Norte", "temperatura": 10, "humedad": 50, "viento": 20, "fecha": "2026-04-10", "alertas": ["roja"]},
        {"zona": "Norte", "temperatura": 20, "humedad": 60, "viento": 10, "fecha": "2026-04-11", "alertas": []},
        {"zona": "Sur", "temperatura": 30, "humedad": 40, "viento": 40, "fecha": "2026-04-12", "alertas": ["amarilla", "naranja"]}
    ]

    # 2. EJECUTAMOS LA FUNCIÓN
    stats = calcular_estadisticas(datos)

    # 3. COMPROBACIONES (Asserts)
    
    # Media Temperatura: Norte (10+20)/2 = 15 | Sur = 30
    assert stats["media_temperatura_zona"]["Norte"] == 15.0
    assert stats["media_temperatura_zona"]["Sur"] == 30.0

    # Máximo Viento: El valor más alto es 40
    assert stats["max_viento"] == 40.0

    # Número de Alertas: 1 (roja) + 0 + 2 (amarilla, naranja) = 3
    assert stats["numero_alertas"] == 3

def test_estadisticas_lista_vacia():
    # Prueba que el sistema no explote si no hay datos
    datos = []
    stats = calcular_estadisticas(datos)
    
    assert stats["max_viento"] == 0
    assert stats["media_temperatura_zona"] == {}
    assert stats["numero_alertas"] == 0

def test_conteo_fechas():
    # Probamos si detecta registros de "hoy"
    hoy_str = pd.Timestamp.today().strftime('%Y-%m-%d')
    datos = [
        {"zona": "Norte", "temperatura": 20, "humedad": 50, "viento": 10, "fecha": hoy_str}
    ]
    stats = calcular_estadisticas(datos)
    
    assert stats["registros_hoy"] == 1