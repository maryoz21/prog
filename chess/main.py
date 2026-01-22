from enum import Enum

# --- 1. CLASES TEMPORALES (Simulando tus archivos) ---

class Color(Enum):
    BLANCO = 1
    NEGRO = 2

# Simulamos la clase abstracta Board
class BoardTemp:
    def is_in_bounds(self, x: int, y: int) -> bool:
        pass
    def get_piece_at(self, x: int, y: int):
        pass

# Simulamos tu BoardImpl con la lógica del diccionario que hablamos
class BoardImplTemp(BoardTemp):
    def __init__(self):
        self.pieces = {} # Diccionario temporal
        self.size = 8

    def is_in_bounds(self, x: int, y: int) -> bool:
        return 1 <= x <= self.size and 1 <= y <= self.size

    def add_piece(self, piece):
        self.pieces[(piece.get_x(), piece.get_y())] = piece

    def get_piece_at(self, x: int, y: int):
        return self.pieces.get((x, y))

# Simulamos tu clase Piece con los Getters necesarios
class PieceTemp:
    def __init__(self, color: Color, x: int, y: int):
        self.__color = color
        self.__x = x
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    def get_color(self) -> Color:
        return self.__color
    
    # Método abstracto simulado
    def movimientos_posibles(self, board: BoardTemp):
        pass

# --- 2. IMPLEMENTACIÓN DE LA LÓGICA (Lo que hemos trabajado) ---

class PawnTemp(PieceTemp):
    def is_pawn_in_start_position(self) -> bool:
        # Lógica: Negras arriba (7), Blancas abajo (2)
        if self.get_color() == Color.NEGRO:
            return self.get_y() == 7
        if self.get_color() == Color.BLANCO:
            return self.get_y() == 2
        return False

    def movimientos_posibles(self, board: BoardTemp):
        moves = []
        x, y = self.get_x(), self.get_y()
        # Dirección: Blancas suben (+1), Negras bajan (-1)
        dy = 1 if self.get_color() == Color.BLANCO else -1
        
        # A) Movimiento normal (1 paso)
        next_y = y + dy
        if board.is_in_bounds(x, next_y) and board.get_piece_at(x, next_y) is None:
            moves.append((x, next_y))
            
            # B) Doble salto (Solo si el paso 1 estaba libre y es posición inicial)
            if self.is_pawn_in_start_position():
                doble_y = y + (2 * dy)
                if board.is_in_bounds(x, doble_y) and board.get_piece_at(x, doble_y) is None:
                    moves.append((x, doble_y))
        
        # C) Capturas (Diagonales)
        for dx in [-1, 1]:
            diag_x = x + dx
            diag_y = y + dy
            if board.is_in_bounds(diag_x, diag_y):
                pieza = board.get_piece_at(diag_x, diag_y)
                if pieza and pieza.get_color() != self.get_color():
                    moves.append((diag_x, diag_y))
        return moves

class RookTemp(PieceTemp):
    def movimientos_posibles(self, board: BoardTemp):
        moves = []
        # Las 4 direcciones rectas
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            cx, cy = self.get_x() + dx, self.get_y() + dy
            
            # Bucle "mientras pueda deslizarme"
            while board.is_in_bounds(cx, cy):
                p = board.get_piece_at(cx, cy)
                if p is None:
                    moves.append((cx, cy)) # Casilla vacía
                else:
                    if p.get_color() != self.get_color():
                        moves.append((cx, cy)) # Captura
                    break # Choca y para
                
                cx += dx
                cy += dy
        return moves

# --- 3. MAIN DE PRUEBA (Visualización) ---

def imprimir_tablero(board):
    print("\n   1 2 3 4 5 6 7 8")
    print("  +" + "-"*15 + "+")
    for y in range(8, 0, -1):
        linea = f"{y} |"
        for x in range(1, 9):
            p = board.get_piece_at(x, y)
            if p:
                tipo = "P" if isinstance(p, PawnTemp) else "T"
                col = "B" if p.get_color() == Color.BLANCO else "N"
                linea += f"{tipo}{col}"
            else:
                linea += " ."
        print(linea + "|")
    print("  +" + "-"*15 + "+")

if __name__ == "__main__":
    # Inicializamos tablero temporal
    tablero = BoardImplTemp()

    # Escenario:
    # 1. Torre Blanca en el centro
    torre = RookTemp(Color.BLANCO, 4, 4)
    # 2. Peón Negro "víctima" arriba
    peon_enemigo = PawnTemp(Color.NEGRO, 4, 7)
    # 3. Peón Blanco que bloquea a su torre abajo
    peon_amigo = PawnTemp(Color.BLANCO, 4, 3)
    # 4. Peón de salida normal
    peon_salida = PawnTemp(Color.BLANCO, 2, 2)

    # Añadimos
    tablero.add_piece(torre)
    tablero.add_piece(peon_enemigo)
    tablero.add_piece(peon_amigo)
    tablero.add_piece(peon_salida)

    imprimir_tablero(tablero)

    print(f"Torre en (4,4) puede ir a: {torre.movimientos_posibles(tablero)}")
    print(f"Peón Salida en (2,2) puede ir a: {peon_salida.movimientos_posibles(tablero)}")
    print(f"Peón Enemigo en (4,7) puede ir a: {peon_enemigo.movimientos_posibles(tablero)}")