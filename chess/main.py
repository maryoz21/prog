from board_impl import BoardImpl
from pieces import Pawn, King, Rook, Color, PieceType
from MatchesService import MatchesService

def ejecutar_bateria_de_pruebas() -> bool:
    todo_correcto = True

    # ---------------------------------------------------------
    # TEST 1: ENROQUE CORTO
    # ---------------------------------------------------------
    b1 = BoardImpl()
    b1.add_piece(King(Color.WHITE, 5, 1))
    b1.add_piece(Rook(Color.WHITE, 8, 1))
    b1.add_piece(King(Color.BLACK, 5, 8)) # Rey enemigo obligatorio
    
    if not b1.move_piece(5, 1, 7, 1):
        print("❌ FALLO: Enroque Corto (El rey no pudo saltar).")
        todo_correcto = False
    elif b1.get_piece_at(6, 1) is None or b1.get_piece_at(6, 1).get_type_of_piece() != PieceType.ROOK:
        print("❌ FALLO: Enroque Corto (La torre no se teletransportó a la casilla f1).")
        todo_correcto = False

    # ---------------------------------------------------------
    # TEST 2: ENROQUE LARGO
    # ---------------------------------------------------------
    b2 = BoardImpl()
    b2.add_piece(King(Color.WHITE, 5, 1))
    b2.add_piece(Rook(Color.WHITE, 1, 1))
    b2.add_piece(King(Color.BLACK, 5, 8))
    
    if not b2.move_piece(5, 1, 3, 1):
        print("❌ FALLO: Enroque Largo (El rey no pudo saltar).")
        todo_correcto = False
    elif b2.get_piece_at(4, 1) is None or b2.get_piece_at(4, 1).get_type_of_piece() != PieceType.ROOK:
        print("❌ FALLO: Enroque Largo (La torre no se teletransportó a la casilla d1).")
        todo_correcto = False

    # ---------------------------------------------------------
    # TEST 3: CAPTURA AL PASO (Y borrar el peón fantasma)
    # ---------------------------------------------------------
    b3 = BoardImpl()
    b3.add_piece(King(Color.WHITE, 1, 1))
    b3.add_piece(King(Color.BLACK, 8, 8))
    b3.add_piece(Pawn(Color.WHITE, 5, 5))
    b3.add_piece(Pawn(Color.BLACK, 4, 7))
    
    b3.move_piece(4, 7, 4, 5) # El negro avanza 2 casillas
    
    if not b3.move_piece(5, 5, 4, 6): # El blanco come en diagonal al paso
        print("❌ FALLO: Captura al paso (El motor bloqueó el movimiento legal).")
        todo_correcto = False
    elif b3.get_piece_at(4, 5) is not None:
        print("❌ FALLO: Captura al paso (El peón negro no desapareció del tablero).")
        todo_correcto = False

    # ---------------------------------------------------------
    # TEST 4: CORONACIÓN DE PEÓN
    # ---------------------------------------------------------
    b4 = BoardImpl()
    b4.add_piece(King(Color.WHITE, 1, 1))
    b4.add_piece(King(Color.BLACK, 8, 8))
    b4.add_piece(Pawn(Color.WHITE, 1, 7)) # Peón blanco a punto de llegar
    
    if not b4.move_piece(1, 7, 1, 8):
        print("❌ FALLO: Coronación (El peón no pudo avanzar a la última fila).")
        todo_correcto = False
    else:
        pieza_coronada = b4.get_piece_at(1, 8)
        if pieza_coronada is None or pieza_coronada.get_type_of_piece() != PieceType.QUEEN:
            print("❌ FALLO: Coronación (La pieza no se transformó en Reina).")
            todo_correcto = False

    # ---------------------------------------------------------
    # TEST 5: PIEZA CLAVADA (Prohibir movimiento suicida)
    # ---------------------------------------------------------
    b5 = BoardImpl()
    b5.add_piece(King(Color.WHITE, 5, 1))
    b5.add_piece(Rook(Color.WHITE, 5, 2)) # Esta torre protege al rey
    b5.add_piece(Rook(Color.BLACK, 5, 8)) # Esta torre amenaza toda la columna
    b5.add_piece(King(Color.BLACK, 1, 8))
    
    # Intentamos apartar la torre blanca. NO debería dejarnos porque el rey moriría.
    if b5.move_piece(5, 2, 6, 2):
        print("❌ FALLO: Pieza clavada (El motor permitió un movimiento suicida).")
        todo_correcto = False

    # ---------------------------------------------------------
    # TEST 6: PARTIDA COMPLETA Y DETECCIÓN DE JAQUE MATE
    # ---------------------------------------------------------
    srv = MatchesService()
    srv.create_match(1)
    
    # Jugamos el Mate del Pastor
    srv.move(1, 5, 2, 5, 4) # Blanca e4
    srv.move(1, 5, 7, 5, 5) # Negra e5
    srv.move(1, 6, 1, 3, 4) # Blanca Ac4
    srv.move(1, 2, 8, 3, 6) # Negra Cc6
    srv.move(1, 4, 1, 8, 5) # Blanca Dh5
    srv.move(1, 7, 8, 6, 6) # Negra Cf6
    srv.move(1, 8, 5, 6, 7) # Blanca Dxf7 (Mate)
    
    tablero_final = srv.matches[0].get_board()
    if not tablero_final.is_checkmate(Color.BLACK):
        print("❌ FALLO: Jaque Mate (El motor no detectó la victoria).")
        todo_correcto = False

    return todo_correcto

if __name__ == "__main__":
    resultado = ejecutar_bateria_de_pruebas()
    print(resultado)