from MatchesService import MatchesService
from match import Match

def main():
    print("Iniciando el motor de ajedrez...")

    # 1. Creamos el servicio y la partida
    servicio = MatchesService()
    partida_id = 1
    nueva_partida = Match(id=partida_id, player1="Jugador Blanco", player2="Jugador Negro")
    servicio.matches.append(nueva_partida)

    # 2. Colocamos las 32 piezas
    servicio.start_position(match_id=partida_id)
    tablero = nueva_partida.get_board()

    print("\n--- TABLERO INICIAL ---")
    tablero.print_board()

    # ==========================================
    # DESPEJANDO EL CAMINO PARA EL ENROQUE CORTO
    # ==========================================

    # TURNO 1
    # Blancas: Peón 'e' avanza (e2 a e4)
    servicio.move(partida_id, 5, 2, 5, 4)
    # Negras: Peón 'e' avanza (e7 a e5)
    servicio.move(partida_id, 5, 7, 5, 5)

    # TURNO 2
    # Blancas: Caballo sale (g1 a f3) -> Despeja casilla 7
    servicio.move(partida_id, 7, 1, 6, 3)
    # Negras: Caballo sale (b8 a c6)
    servicio.move(partida_id, 2, 8, 3, 6)

    # TURNO 3
    # Blancas: Alfil sale (f1 a c4) -> Despeja casilla 6
    servicio.move(partida_id, 6, 1, 3, 4)
    # Negras: Peón 'a' avanza (a7 a a6)
    servicio.move(partida_id, 1, 7, 1, 6)

    print("\n--- CAMINO DESPEJADO (El Rey y la Torre se miran) ---")
    tablero.print_board()

    # ==========================================
    # ¡EL MOMENTO DEL ENROQUE!
    # ==========================================
    
    # TURNO 4
    # Blancas: El Rey da su salto de 2 casillas hacia la derecha (e1 a g1) -> (x=5 a x=7)
    print("\n--- TURNO BLANCAS: ¡ENROQUE CORTO! ---")
    exito = servicio.move(partida_id, 5, 1, 7, 1)

    if exito:
        print("✅ ¡Enroque aceptado! Rey y Torre se han movido a la vez.")
    else:
        print("❌ Movimiento ilegal (Revisa los if de __enroque)")

    # Imprimimos el tablero final para ver la magia
    tablero.print_board()

if __name__ == "__main__":
    main()