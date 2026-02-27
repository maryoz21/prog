from MatchesService import MatchesService
from match import Match


print("Iniciando el motor de ajedrez...")

# 1. Creamos el servicio que gestiona las partidas
servicio = MatchesService()

# 2. Creamos una partida y la metemos en la lista del servicio
# (Hacemos esto a mano porque el método create_match y add_match los tenías con 'pass')
partida_id = 1
nueva_partida = Match(id=partida_id, player1="Jugador Blanco", player2="Jugador Negro")
servicio.matches.append(nueva_partida)

# 3. Llamamos a la función que hiciste para colocar las piezas iniciales
print("Colocando las piezas en sus casillas iniciales...")
servicio.start_position(match_id=partida_id)

# 4. Sacamos el tablero de la partida y lo imprimimos
tablero = nueva_partida.get_board()
tablero.print_board()

print("\n--- TURNO DE LAS BLANCAS: Moviendo Peón de e2 a e4 ---")
# Movemos la pieza en x=5, y=2 (Peón Rey Blanco) a x=5, y=4
exito = servicio.move(match_id=partida_id, from_x=5, from_y=2, to_x=5, to_y=4)

if exito:
    print("¡Movimiento aceptado!")
else:
    print("Movimiento ilegal")

# Volvemos a imprimir el tablero para ver cómo el peón ha avanzado 2 casillas
tablero.print_board()

print("a")