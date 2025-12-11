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

@app.get("/usuarios")
def obtener_usuarios():
    collection = db.collection("usuarios").stream()
    return [c.to_dict() for c in collection]


@app.get("/cursos")
def obtener_cursos():
    collection = db.collection("cursos").stream()
    return [c.to_dict() for c in collection]
