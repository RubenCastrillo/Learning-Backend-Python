from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configuración de Jinja2 para cargar plantillas desde la carpeta "templates"
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/procesar_formulario/", response_class=HTMLResponse)
async def procesar_formulario(request: Request, nombre: str = Form(...), email: str = Form(...)):
    # Aquí puedes procesar los datos recibidos del formulario si es necesario
    return templates.TemplateResponse("respuesta.html", {"request": request, "nombre": nombre, "email": email})
