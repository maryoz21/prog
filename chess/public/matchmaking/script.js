document.addEventListener('DOMContentLoaded', async () => {
    await loadAvailableUsers();
});

// Función asíncrona para pedir usuarios al servidor
async function loadAvailableUsers() {
    const grid = document.getElementById('users-grid');
    const status = document.getElementById('status');
    const currentUser = localStorage.getItem('chessUsername');

    try {
        const response = await fetch('/api/users');
        
        if (!response.ok) throw new Error('Error al obtener lista');

        const users = await response.json();
        
        renderUsers(users.filter(u => u.username !== currentUser), grid);
        status.textContent = `${users.length} jugadores encontrados`;

    } catch (error) {
        console.warn('Backend no disponible, cargando datos simulados...', error);
        
        // Mock Data para pruebas
        const mockUsers = [
            { username: "Kasparov_Bot", rank: 2800 },
            { username: "DeepBlue", rank: 2700 },
            { username: "Novato123", rank: 1200 }
        ];
        renderUsers(mockUsers, grid);
        status.textContent = "Modo Demo (Backend desconectado)";
    }
}

// Función auxiliar para dibujar el HTML
function renderUsers(users, container) {
    container.innerHTML = '';
    users.forEach(user => {
        const card = document.createElement('div');
        card.className = 'user-card';
        card.innerHTML = `
            <div class="avatar">♟️</div>
            <span class="username">${user.username}</span>
            <button class="play-btn" onclick="challengePlayer('${user.username}')">
                Desafiar
            </button>
        `;
        container.appendChild(card);
    });
}

// Función asíncrona para iniciar el reto
async function challengePlayer(rivalName) {
    const currentUser = localStorage.getItem('chessUsername');
    
    if(!confirm(`¿Quieres iniciar una partida contra ${rivalName}?`)) return;

    try {
        // Petición para crear la partida en el servidor
        const response = await fetch('/api/create-match', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ 
                white: currentUser, 
                black: rivalName 
            })
        });

        if (response.ok) {
            const matchData = await response.json();
            alert(`Partida creada! ID: ${matchData.id}`);
            // Redirigir al tablero
            // window.location.href = `../game/board.html?matchId=${matchData.id}`;
        } else {
            throw new Error("El servidor rechazó la partida");
        }

    } catch (error) {
        console.error(error);
        alert(`Error: No se pudo conectar con ${rivalName}. (Simulación: Empezando partida local...)`);
        // Fallback para pruebas
        // window.location.href = `../game/board.html?rival=${rivalName}`;
    }
}