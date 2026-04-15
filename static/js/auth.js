document.addEventListener("DOMContentLoaded", () => {
    // 1. Intentamos obtener los formularios (Asegúrate de poner estos IDs en tu HTML)
    const loginForm = document.getElementById("loginForm");
    const registroForm = document.getElementById("registroForm");

    // Función genérica para mostrar errores
    const showError = (elementId, message) => {
        const errorElement = document.getElementById(elementId);
        if (errorElement) errorElement.textContent = message;
    };

    const validateEmail = (email) => {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    };

    // --- LÓGICA PARA LOGIN ---
    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            let valid = true;
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value.trim();

            showError("emailError", "");
            showError("passwordError", "");

            if (!validateEmail(email)) {
                showError("emailError", "Introduce un correo válido.");
                valid = false;
            }
            if (password.length === 0) {
                showError("passwordError", "La contraseña es obligatoria.");
                valid = false;
            }

            if (!valid) e.preventDefault();
        });
    }

    // --- LÓGICA PARA REGISTRO ---
    if (registroForm) {
        registroForm.addEventListener("submit", (e) => {
            let valid = true;
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value.trim();
            const confirmPassword = document.getElementById("confirm_password").value.trim();

            showError("emailError", "");
            showError("passwordError", "");
            showError("confirmPasswordError", "");

            if (!validateEmail(email)) {
                showError("emailError", "Email no válido.");
                valid = false;
            }
            if (password.length < 6) {
                showError("passwordError", "Mínimo 6 caracteres.");
                valid = false;
            }
            if (password !== confirmPassword) {
                showError("confirmPasswordError", "Las contraseñas no coinciden.");
                valid = false;
            }

            if (!valid) e.preventDefault();
        });
    }
});