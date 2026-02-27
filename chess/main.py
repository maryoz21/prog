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

print("\n--- MOVIENDO PEÓN a b8 PARA COMER CABALLO Y CORONAR ---")
# Cambiamos el destino a x=2, y=8 (b8) para comer en diagonal
tablero.move_piece(1, 7, 2, 8) 
tablero.print_board()

print("a")