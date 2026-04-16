document.addEventListener("DOMContentLoaded", () => {
    // 1. Captura de formularios
    const loginForm = document.getElementById("loginForm");
    const registroForm = document.getElementById("registroForm");

    // 2. Utilidades de validación
    const showError = (elementId, message) => {
        const errorElement = document.getElementById(elementId);
        if (errorElement) {
            errorElement.textContent = message;
            errorElement.style.color = "red"; // Un poco de estilo rápido
        }
    };

    const validateEmail = (email) => {
        // Combinamos la regex más completa que teníais
        return /^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$/.test(email);
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
                showError("emailError", "Email no válido (ejemplo@dominio.com).");
                valid = false;
            }
            if (password.length < 6) {
                showError("passwordError", "La contraseña debe tener al menos 6 caracteres.");
                valid = false;
            }
            if (password !== confirmPassword) {
                showError("confirmPasswordError", "¡Cuidado! Las contraseñas no coinciden.");
                valid = false;
            }

            if (!valid) e.preventDefault();
        });
    }
});