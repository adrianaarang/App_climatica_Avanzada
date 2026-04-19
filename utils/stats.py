# Importamos pandas para trabajar con los registros como tabla
import pandas as pd

# Importamos matplotlib para generar gráficas
import matplotlib
matplotlib.use('Agg')  # backend sin pantalla para servidores
import matplotlib.pyplot as plt

# Importamos os para crear carpetas si no existen
import os


def calcular_estadisticas(registros):
    """
    Calcula estadísticas a partir de los registros meteorológicos.

    Usa pandas para:
    - agrupar datos por zona
    - calcular medias
    - contar alertas
    - filtrar por fechas
    """

    # Si no hay registros, devolvemos estadísticas vacías
    if not registros:
        return {
            "media_temperatura_zona": {},
            "media_humedad_zona": {},
            "max_viento": 0,
            "numero_alertas": 0,
            "registros_hoy": 0,
            "registros_semana": 0,
            "registros_mes": 0
        }

    # Convertimos la lista de registros en un DataFrame de pandas
    df = pd.DataFrame(registros)

    # Convertimos la columna fecha a tipo fecha
    # errors="coerce" convierte errores en NaT en lugar de romper el programa
    df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    # Si no existe la columna alertas, la creamos con listas vacías
    if "alertas" not in df.columns:
        df["alertas"] = [[] for _ in range(len(df))]

    # Nos aseguramos de que cada valor de alertas sea una lista
    df["alertas"] = df["alertas"].apply(
        lambda x: x if isinstance(x, list) else []
    )

    # ---------------------------
    # MEDIA DE TEMPERATURA POR ZONA
    # ---------------------------
    media_temperatura_zona = (
        df.groupby("zona")["temperatura"]
        .mean()
        .round(2)
        .to_dict()
    )

    # ---------------------------
    # MEDIA DE HUMEDAD POR ZONA
    # ---------------------------
    media_humedad_zona = (
        df.groupby("zona")["humedad"]
        .mean()
        .round(2)
        .to_dict()
    )

    # ---------------------------
    # MÁXIMO VIENTO REGISTRADO
    # ---------------------------
    max_viento = float(df["viento"].max()) if not df["viento"].empty else 0

    # ---------------------------
    # NÚMERO TOTAL DE ALERTAS
    # ---------------------------
    numero_alertas = int(df["alertas"].apply(len).sum())

    # ---------------------------
    # REGISTROS DE HOY / SEMANA / MES
    # ---------------------------
    hoy = pd.Timestamp.today().normalize()
    hace_7_dias = hoy - pd.Timedelta(days=7)
    hace_30_dias = hoy - pd.Timedelta(days=30)

    registros_hoy = int((df["fecha"].dt.normalize() == hoy).sum())
    registros_semana = int((df["fecha"] >= hace_7_dias).sum())
    registros_mes = int((df["fecha"] >= hace_30_dias).sum())

    # Devolvemos todas las estadísticas en un diccionario
    return {
        "media_temperatura_zona": media_temperatura_zona,
        "media_humedad_zona": media_humedad_zona,
        "max_viento": max_viento,
        "numero_alertas": numero_alertas,
        "registros_hoy": registros_hoy,
        "registros_semana": registros_semana,
        "registros_mes": registros_mes
    }


def generar_graficas(registros):
    """
    Genera gráficas a partir de los registros y las guarda como imágenes
    dentro de static/img para poder mostrarlas en estadisticas.html.
    """

    # Si no hay registros, no generamos nada
    if not registros:
        return

    # Creamos la carpeta static/img si no existe
    os.makedirs("static/img", exist_ok=True)

    # Convertimos los registros a DataFrame
    df = pd.DataFrame(registros)

    # Si el DataFrame está vacío, salimos
    if df.empty:
        return

    # ---------------------------
    # GRÁFICA 1: TEMPERATURA MEDIA POR ZONA
    # ---------------------------
    temperatura_media = df.groupby("zona")["temperatura"].mean().sort_values()

    plt.figure(figsize=(10, 5))
    temperatura_media.plot(kind="bar")
    plt.title("Temperatura media por zona")
    plt.xlabel("Zona")
    plt.ylabel("Temperatura media (ºC)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("static/img/temperatura_media.png")
    plt.close()

    # ---------------------------
    # GRÁFICA 2: HUMEDAD MEDIA POR ZONA
    # ---------------------------
    humedad_media = df.groupby("zona")["humedad"].mean().sort_values()

    plt.figure(figsize=(10, 5))
    humedad_media.plot(kind="bar")
    plt.title("Humedad media por zona")
    plt.xlabel("Zona")
    plt.ylabel("Humedad media (%)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("static/img/humedad_media.png")
    plt.close()

    # ---------------------------
    # GRÁFICA 3: NÚMERO DE REGISTROS POR ZONA
    # ---------------------------
    registros_por_zona = df["zona"].value_counts().sort_values()

    plt.figure(figsize=(10, 5))
    registros_por_zona.plot(kind="bar")
    plt.title("Número de registros por zona")
    plt.xlabel("Zona")
    plt.ylabel("Cantidad de registros")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("static/img/registros_por_zona.png")
    plt.close()
