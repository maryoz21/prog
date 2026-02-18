from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import uvicorn

# --- IMPORTAMOS TU LÓGICA DE AJEDREZ ---
# "from backend" se refiere a la carpeta. 
# "MatchesService" al archivo. 
# "MatchesService" (el segundo) a la Clase dentro del archivo.
from backend.MatchesService import MatchesService 

app = FastAPI()

# --- CONFIGURACIÓN DE SEGURIDAD (CORS) ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- INICIALIZAMOS TU SERVICIO DE AJEDREZ ---
# Esto arranca tu lógica "global" para gestionar las partidas
chess_service = MatchesService()

# --- MODELOS DE DATOS (Lo que envía el Frontend) ---
class CreateMatchRequest(BaseModel):
    white: str  # Nombre jugador blancas
    black: str  # Nombre jugador negras

class MoveRequest(BaseModel):
    match_id: str
    from_pos: str # Ej: "e2"
    to_pos: str   # Ej: "e4"

# --- RUTAS DE LA API (Los @app) ---

# 1. Ruta para Registrar Usuarios (Simplificada)
@app.post("/api/register")
async def register(data: dict):
    # Aquí podrías conectar con una base de datos real
    return {"success": True, "message": "Usuario registrado"}

# 2. Ruta para Crear Partida
@app.post("/api/create-match")
async def create_match(request: CreateMatchRequest):
    try:
        # LLAMADA A TU LÓGICA:
        # Asumo que tu MatchesService tiene un método create_match
        new_match = chess_service.create_match(request.white, request.black)
        
        # Asumo que new_match tiene un atributo .id
        return {"success": True, "match_id": new_match.id}
    except Exception as e:
        print(f"Error creando partida: {e}")
        raise HTTPException(status_code=500, detail=str(e))

# 3. Ruta para Mover Ficha
@app.post("/api/move")
async def make_move(request: MoveRequest):
    try:
        # 1. Obtener la partida
        match = chess_service.get_match(request.match_id)
        if not match:
            raise HTTPException(status_code=404, detail="Partida no encontrada")

        # 2. Intentar mover (Usando TU lógica de Board)
        # Asumo que tienes un método move(desde, hasta) que devuelve True/False
        move_success = match.board.move_piece(request.from_pos, request.to_pos)

        if move_success:
            return {"success": True, "message": "Movimiento válido"}
        else:
            return {"success": False, "message": "Movimiento ilegal"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# --- RUTAS DE VISUALIZACIÓN ---

# Redirigir la raíz al landing page
@app.get("/")
async def root():
    return RedirectResponse(url="/landing/index.html")

# Servir los archivos HTML/CSS/JS (Siempre va al final)
app.mount("/", StaticFiles(directory="public", html=True), name="static")

# --- ARRANCAR SERVIDOR ---
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)