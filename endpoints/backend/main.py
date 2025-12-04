from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI()

# Configuración CORS (para que el HTML funcione)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- 1. MODELO DE DATOS (Simulando tu User) ---
class User(BaseModel):
    id: Optional[int] = None
    name: str
    birth_date: date

# --- 2. BASE DE DATOS FALSA (En memoria) ---
# Iniciamos con un usuario de prueba para que no salga vacía la lista
users_db = [
    {"id": 1, "name": "Usuario Test", "birth_date": date(1995, 5, 20)},
    {"id": 2, "name": "Maria Ejemplo", "birth_date": date(2000, 10, 1)}
]
last_id = 2

# --- 3. FUNCIONES AUXILIARES (Simulando tu lógica de filtros) ---
def calculate_age(birth_date: date) -> int:
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# --- 4. ENDPOINTS (CRUD) ---

# GET - LISTAR (Con filtros simulados)
@app.get("/users", response_model=List[User])
def list_users(
    search: Optional[str] = Query(None),
    min_age: int = Query(-1)
):
    # Empezamos con todos los usuarios
    result = list(users_db)
    
    # 1. Filtro por nombre
    if search:
        # Filtramos si el nombre contiene el texto (case insensitive)
        result = [u for u in result if search.lower() in u["name"].lower()]
    
    # 2. Filtro por edad
    if min_age > -1:
        filtered_by_age = []
        for u in result:
            # Calculamos la edad al vuelo
            age = calculate_age(u["birth_date"])
            if age >= min_age:
                filtered_by_age.append(u)
        result = filtered_by_age

    return result

# GET - LEER UNO
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# POST - CREAR
@app.post("/users", response_model=User)
def create_user(user: User):
    global last_id
    last_id += 1
    
    new_user = user.dict()
    new_user["id"] = last_id # Asignamos ID nuevo
    
    users_db.append(new_user)
    return new_user

# PUT - ACTUALIZAR
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_input: User):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            # Actualizamos los datos manteniendo el ID
            updated_user = user_input.dict()
            updated_user["id"] = user_id
            users_db[index] = updated_user
            return updated_user
            
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

# DELETE - BORRAR
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users_db):
        if user["id"] == user_id:
            del users_db[index]
            return {"msg": "Usuario eliminado correctamente"}
            
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)