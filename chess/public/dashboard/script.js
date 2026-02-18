document.addEventListener('DOMContentLoaded', async () => {
    // 1. Verificar sesión antes de mostrar nada
    await initDashboard();
    
    // 2. Configurar los botones del menú
    setupMenuActions();
});

// Función de inicio asíncrona
async function initDashboard() {
    const username = localStorage.getItem('chessUsername');
    const displayElement = document.getElementById('displayUsername');

    // Simulación de checkeo de token (útil si tuvieras backend real)
    try {
        if (!username) throw new Error("No hay usuario");
        
        // Aquí podrías hacer: await fetch('/api/validate-session');
        
        displayElement.textContent = username;
        console.log(`Dashboard cargado para: ${username}`);

    } catch (error) {
        console.warn("Sesión no válida, redirigiendo...");
        window.location.href = '../landing/index.html';
    }
}

function setupMenuActions() {
    // --- ACCIÓN: JUGAR ---
    const playCard = document.getElementById('card-play');
    playCard.addEventListener('click', async () => {
        // Efecto visual o lógica previa a navegar
        playCard.style.opacity = '0.5'; 
        // Navegar al matchmaking
        window.location.href = '../matchmaking/users.html';
    });

    // --- ACCIÓN: OPCIONES ---
    document.getElementById('card-options').addEventListener('click', async () => {
        alert("Menú de opciones: Aquí podrás cambiar el tema del tablero.");
    });

    // --- ACCIÓN: HISTORIAL ---
    document.getElementById('card-history').addEventListener('click', async () => {
        // Ejemplo de cómo cargarías datos asíncronamente
        await loadHistory();
    });

    // --- ACCIÓN: PERFIL ---
    document.getElementById('card-profile').addEventListener('click', () => {
        const user = localStorage.getItem('chessUsername');
        alert(`Perfil de Usuario\nNombre: ${user}\nELO: 1200 (Provisional)`);
    });

    // --- LOGOUT ---
    document.getElementById('btn-logout').addEventListener('click', () => {
        if(confirm("¿Cerrar sesión?")) {
            localStorage.removeItem('chessUsername');
            window.location.href = '../landing/index.html';
        }
    });
}

// Función simulada para cargar historial
async function loadHistory() {
    try {
        // const res = await fetch('/api/history');
        // const data = await res.json();
        alert("Cargando historial de partidas del servidor... (Simulado: Sin partidas recientes)");
    } catch (e) {
        console.error("Error cargando historial");
    }
}