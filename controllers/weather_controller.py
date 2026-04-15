# controllers/weather_controller.py
from flask import render_template, request, redirect, url_for, flash
import json
import os

def registrar_clima():
    # Si el usuario envía el formulario
    if request.method == 'POST':
        # 1. Recoger datos
        nuevo_dato = {
            "fecha": request.form.get('fecha'),
            "zona": request.form.get('zona'),
            "temperatura": float(request.form.get('temperatura')),
            "humedad": int(request.form.get('humedad')),
            "viento": float(request.form.get('viento')),
            "lluvia": float(request.form.get('lluvia'))
        }

        # 2. Ruta al archivo de datos
        ruta_json = os.path.join('data', 'registros.json')

        # 3. Leer y Guardar
        datos = []
        if os.path.exists(ruta_json):
            with open(ruta_json, 'r', encoding='utf-8') as f:
                try:
                    datos = json.load(f)
                except:
                    datos = []

        datos.append(nuevo_dato)

        with open(ruta_json, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

        return "<h1>✅ ¡Datos guardados!</h1><a href='/registrar'>Volver</a>"

    # Si el usuario solo entra a la página, mostramos el HTML
    return render_template('interfaz_tiempo.html')