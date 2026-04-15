// static/js/weather.js

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    
    // Si el formulario existe en la página
    if (form) {
        console.log("✅ Weather.js cargado y formulario detectado");

        form.addEventListener('submit', (e) => {
            const temp = document.getElementsByName('temperatura')[0].value;
            const humedad = document.getElementsByName('humedad')[0].value;

            // Validación de temperatura extrema
            if (temp > 50 || temp < -50) {
                if (!confirm("⚠️ ¿Estás seguro de que la temperatura es correcta? Parece un valor extremo.")) {
                    e.preventDefault(); // Cancela el envío si el usuario dice que NO
                    return;
                }
            }

            // Validación de humedad (0-100)
            if (humedad < 0 || humedad > 100) {
                alert("❌ La humedad debe estar entre 0 y 100%");
                e.preventDefault(); // Cancela el envío
                return;
            }
            
            console.log("🚀 Enviando datos climáticos...");
        });
    } else {
        console.error("❌ No se encontró el formulario en esta página");
    }
});