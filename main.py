from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# =========================
# CONFIGURACIÓN
# =========================

templates = Jinja2Templates(directory="./templates")

app.mount("/static", StaticFiles(directory="./static"), name="static")


# =========================
# INICIO
# =========================
@app.get("/", response_class=HTMLResponse)
def inicio():

    return """
    <h1>Proyecto funcionando ✅</h1>

    <ul>
        <li><a href="/pendientes">Pendientes</a></li>
        <li><a href="/vocales/hola">Vocales</a></li>
        <li><a href="/temperatura/30">Temperatura</a></li>
    </ul>
    """


# =========================
# RUTA /pendientes
# =========================
@app.get("/pendientes", response_class=HTMLResponse)
def pendientes(request: Request):

    tareas = [
        {"descripcion": "Hacer tarea de matemáticas", "completada": False},
        {"descripcion": "Estudiar inglés", "completada": True},
        {"descripcion": "Leer un libro", "completada": False},
        {"descripcion": "Ordenar el cuarto", "completada": True},
    ]

    return templates.TemplateResponse(
        "pendientes.html",
        {
            "request": request,
            "tareas": tareas
        }
    )


# =========================
# RUTA /vocales/{frase}
# =========================
@app.get("/vocales/{frase}", response_class=HTMLResponse)
def vocales(request: Request, frase: str):

    letras = list(frase)

    return templates.TemplateResponse(
        "vocales.html",
        {
            "request": request,
            "letras": letras
        }
    )


# =========================
# RUTA /temperatura/{grados}
# =========================
@app.get("/temperatura/{grados}", response_class=HTMLResponse)
def temperatura(request: Request, grados: int):

    if grados < 10:
        estado = "Frío"
    elif grados < 25:
        estado = "Templado"
    elif grados < 35:
        estado = "Caluroso"
    else:
        estado = "Extremo"

    return templates.TemplateResponse(
        "temperatura.html",
        {
            "request": request,
            "grados": grados,
            "estado": estado
        }
    )