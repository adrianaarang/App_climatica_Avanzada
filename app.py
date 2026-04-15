from flask import Flask, render_template, request, redirect, url_for, session, flash
from controllers.auth_controller import AuthController
from controllers.weather_controller import WeatherController
from controllers.alert_controller import AlertController 
from utils.logger_config import configurar_logger

logger = configurar_logger()

app = Flask(__name__)
app.secret_key = "clave_secreta_provisional"

auth_controller = AuthController()
weather_controller = WeatherController()



# INICIO
@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/auth/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        exito, mensaje = auth_controller.iniciar_sesion(email, password)

        if exito:
            session["usuario"] = email
            return redirect(url_for("interfaz_tiempo"))
        else:
            flash(mensaje) # Esto guarda el mensaje en la "mochila" de la sesión
            return redirect(url_for('login'))
    return render_template("login.html")



@app.route("/auth/register", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        exito, mensaje = auth_controller.registrar_usuario(email, password)

        if exito:
            return redirect(url_for("login"))

        return render_template("registro.html", mensaje=mensaje)

    return render_template("registro.html")













# LOGOUT
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("inicio"))


# INTERFAZ PRINCIPAL
@app.route("/interfaz_tiempo")
def interfaz_tiempo():
    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("interfaz_tiempo.html", usuario=session["usuario"])


# GUARDAR DATOS CLIMÁTICOS
@app.route("/guardar_datos", methods=["POST"])
def guardar_datos():
    if "usuario" not in session:
        return redirect(url_for("login"))

    datos = {
        "fecha": request.form.get("fecha", "").strip(),
        "zona": request.form.get("zona", "").strip(),
        "temperatura": request.form.get("temperatura", "").strip(),
        "humedad": request.form.get("humedad", "").strip(),
        "viento": request.form.get("viento", "").strip(),
        "lluvia": request.form.get("lluvia", "").strip()
    }

    exito, mensaje, alertas = weather_controller.guardar_registro(datos)

    return render_template(
        "interfaz_tiempo.html",
        usuario=session["usuario"],
        mensaje=mensaje,
        alertas=alertas if exito else []
    )


# CONSULTA POR ZONA
@app.route("/consulta", methods=["GET", "POST"])
def consulta():
    if "usuario" not in session:
        return redirect(url_for("login"))

    registros = []
    zona_buscada = ""

    if request.method == "POST":
        zona_buscada = request.form.get("zona", "").strip()
        registros = weather_controller.consultar_por_zona(zona_buscada)

    return render_template(
        "consulta_zona.html",
        registros=registros,
        zona=zona_buscada
    )


# ESTADÍSTICAS
@app.route("/estadisticas")
def estadisticas():
    if "usuario" not in session:
        return redirect(url_for("login"))

    stats = weather_controller.obtener_estadisticas()
    return render_template("estadisticas.html", stats=stats)


if __name__ == "__main__":
    app.run(debug=True)