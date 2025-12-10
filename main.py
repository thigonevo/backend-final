from fastapi import FastAPI
app =FastAPI()
@app.get("/health")
def obtener_salud_sitio():
    return "ok"