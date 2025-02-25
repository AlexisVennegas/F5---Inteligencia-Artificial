from fastapi import FastAPI
from starlette.responses import RedirectResponse
from apis.roles import router as roles_router
from apis.usuarios import router as usuarios_router
from apis.alumnos import router as alumnos_router 
from apis.niveles import router as niveles_router
from apis.profesores import router as profesores_router
from apis.cursos import router as cursos_router
from apis.estudios import router as estudios_router
from apis.grupos import router as grupos_router


tags_metadata = [
    {
        "name": "Roles",
        "description": "Operaciones con roles"
    },
    {
        "name": "Usuarios",
        "description": "Operaciones con usuarios"
    },
    {
        "name": "Alumnos",
        "description": "Operaciones de alumnos"
    },

    {
        "name": "Niveles",
        "description": "Operaciones con niveles"
    },
    {

        "name": "Profesores",
        "description" : "Operaciones con profesores"
    },
    {
        "name": "Cursos",
        "description": "Operaciones con cursos"
    },
    {
        "name": "Inscripcion",
        "description": "Operaciones con inscripciones"
    },
    {
        "name": "Grupos",
        "description": "Operaciones con grupos"
    }
]

app = FastAPI(openapi_tags=tags_metadata, description="API para la gestión de la escuela de danza Fenix")

# Registrar enrutadores

app.include_router(roles_router, prefix="/Roles")
app.include_router(usuarios_router, prefix="/Usuarios")
app.include_router(alumnos_router, prefix ="/Alumnos")
app.include_router(niveles_router, prefix = "/Niveles")
app.include_router(profesores_router, prefix="/Profesores")
app.include_router(cursos_router, prefix="/Cursos")
app.include_router(estudios_router, prefix="/Inscripcion")
app.include_router(grupos_router, prefix="/Grupos")

#################### MAIN #################

@app.get("/")
def main():
    return RedirectResponse(url="/docs")


