document.getElementById('gameForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const usernameInput = document.getElementById('username');
    const username = usernameInput.value.trim();
    const btn = this.querySelector('button');
    
    if (!username) return;

    // Feedback visual de carga
    btn.textContent = "Conectando...";
    btn.disabled = true;

    try {
        // Petición asíncrona al servidor
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: username })
        });

        if (!response.ok) {
            throw new Error(`Error del servidor: ${response.status}`);
        }

        // Si todo va bien, guardamos y redirigimos
        localStorage.setItem('chessUsername', username);
        window.location.href = '../dashboard/dashboard.html';

    } catch (error) {
        console.error('Fallo en el registro:', error);
        
        // FALLBACK: Si no tienes backend real, permitimos entrar igual para probar
        // (En producción, aquí mostrarías un error al usuario)
        alert("Modo Offline: Entrando sin servidor...");
        localStorage.setItem('chessUsername', username);
        window.location.href = '../dashboard/dashboard.html';
        
    } finally {
        // Restaurar botón si falló y no redirigimos
        btn.textContent = "START";
        btn.disabled = false;
    }
});