# 🌦️ App Climática Avanzada

Aplicación web en Flask para registrar, consultar y analizar datos meteorológicos por zonas.

🚀 Python · Flask · Pandas · Matplotlib · JavaScript

---

## ✨ Descripción

App web desarrollada con **Flask** que permite gestionar datos meteorológicos de distintas zonas.

Incluye:
- validación de datos
- sistema de alertas
- almacenamiento en JSON
- estadísticas
- generación de gráficas

---

## 🧠 Funcionalidades

### 🔐 Autenticación
- Registro de usuarios
- Login

### 🌡️ Registro climático
Permite guardar:
- fecha
- zona
- temperatura
- humedad
- viento
- lluvia

### 🚨 Alertas
- calor extremo
- frío extremo
- viento fuerte

### 🔍 Consulta por zona
Filtra registros por zona.

### 📊 Estadísticas
- medias
- máximos
- conteos
- gráficas automáticas

---

## 🏗️ Estructura
``` 
App_climatica_Avanzada/
│
├── app.py
├── data/
├── controllers/
├── models/
├── utils/
├── templates/
├── static/
└── tests/
```
Arquitectura basada en separación de responsabilidades (tipo MVC).
---

## ⚙️ Instalación

### 1. Clonar repositorio

git clone https://github.com/adryeli/App_climatica_Avanzada

cd App_climatica_Avanzada


### 2. Crear entorno virtual

python -m venv .venv
.venv\Scripts\activate


### 3. Instalar dependencias

pip install -r requirements.txt


---

## ▶️ Ejecutar la app

python app.py


Abrir en navegador:

http://127.0.0.1:5000


---

## 📦 Dependencias

Flask==3.1.3
pandas
matplotlib
numpy
pytest


---

## 🔄 Flujo

1. Login / registro  
2. Introducción de datos  
3. Validación  
4. Alertas  
5. Guardado en JSON  
6. Consulta  
7. Estadísticas  

---

## 🧪 Tests

pytest


---

## 📁 Datos

data/usuarios.json
data/registros.json


---

## 📝 Logs

logs/app.log


---

## 🚀 Mejoras futuras

- cifrado de contraseñas  
- base de datos real  
- API REST  
- filtros por fecha  
- exportación  
- mejora UI  

---

## 👩‍💻 Autor

Helen
Adriana 
Leo
Elizabeth
Luis


---

## 📄 Licencia

Uso educativo

