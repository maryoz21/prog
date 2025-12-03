# main.py
from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Permite cualquier origen (ideal para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"mensaje": "Hola desde FastAPI sin usar 'uvicorn' en la terminal!"}

@app.get("/saludo/{nombre}")
def saludo(nombre: str):
    return {"saludo": f"Hola, {nombre}!"}


class Usuario(BaseModel):
    id: int
    nombre: str
    edad: int

@app.post("/usuario")
def crear_usuario(usuario: Usuario, token: str = Header(...)):
    # Simulamos validación de token
    if token != "secreto123":
        raise HTTPException(status_code=401, detail="Token inválido")

    return {
        "mensaje": "Usuario recibido correctamente",
        "usuario": usuario,
    }



if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True  # quita esto si no quieres auto-reload
    )
