from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app =FastAPI()    

@app.get("/health")
def obtener_salud_sitio():
    return "sapo"
class Usuario (BaseModel):
    nombre:str
    email:str
    edad:int
    contraseña:str
    repetir_contraseña:str
class Curso (BaseModel):
    precio:int
    nombre:str
    descripcion:str
    duracion:int

@app.get("/usuarios")
def obtener_usuarios():
    collection = db.collection("usuarios").stream()
    return [c.to_dict() for c in collection]

@app.post("/usuarios")
def crear_usuario (usuario:Usuario):
    if usuario.contraseña != usuario.repetir_contraseña:
        return "Las contraseñas no coinciden"
    del usuario.repetir_contraseña
    db.collection("usuarios").add(usuario.dict())
    return "usuario creado con exito"


@app.get("/cursos")
def obtener_cursos():
    collection = db.collection("cursos").stream()
    return [c.to_dict() for c in collection]

@app.post("/cursos")
def crear_curso (curso:Curso):
    if curso.nombre == "admin":
        return "el nombre no puede llevar admin"
    db.collection("cursos").add(curso.dict())
    return "curso creado con exito"