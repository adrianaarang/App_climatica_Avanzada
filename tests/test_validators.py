import pytest
from datetime import datetime, timedelta
# Importamos todas tus funciones de validación
from utils.validators import (
    validar_fecha, validar_zona, validar_temperatura, 
    validar_humedad, validar_viento, validar_lluvia
)

# --- TESTS DE FECHA ---
def test_fecha_valida():
    assert validar_fecha("2026-04-10") is True
    assert validar_fecha("fecha-loca") is False
    # Test de fecha futura
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    assert validar_fecha(tomorrow) is False

# --- TESTS DE ZONA ---
def test_zona_valida():
    assert validar_zona("Norte") is True
    assert validar_zona("") is False
    assert validar_zona("   ") is False
    assert validar_zona("A" * 51) is False  # Más de 50 caracteres

# --- TESTS DE TEMPERATURA ---
def test_temperatura_rangos():
    assert validar_temperatura(25) is True
    assert validar_temperatura("25.5") is True
    assert validar_temperatura(-51) is False  # Límite inferior
    assert validar_temperatura(61) is False   # Límite superior
    assert validar_temperatura("caliente") is False

# --- TESTS DE HUMEDAD ---
def test_humedad_rangos():
    assert validar_humedad(50) is True
    assert validar_humedad(-1) is False
    assert validar_humedad(101) is False
    assert validar_humedad("mucho") is False

# --- TESTS DE VIENTO ---
def test_viento_rangos():
    assert validar_viento(100) is True
    assert validar_viento(-5) is False
    assert validar_viento(501) is False

# --- TESTS DE LLUVIA ---
def test_lluvia_rangos():
    assert validar_lluvia(0) is True
    assert validar_lluvia(999) is True
    assert validar_lluvia(-1) is False