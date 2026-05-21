from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# carpeta static
app.mount("/static", StaticFiles(directory="static"), name="static")

# carpeta templates
templates = Jinja2Templates(directory="templates")


# ======================
# INICIO
# ======================
@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return """
    <h1>Proyecto funcionando</h1>
    <a href='/vocales/hola'>Ir a vocales</a>
    """


# ======================
# VOCALES
# ======================
@app.get("/vocales/{frase}")
def vocales(frase: str):

    letras = list(frase)

    return {
        "frase": frase,
        "letras": letras
    }