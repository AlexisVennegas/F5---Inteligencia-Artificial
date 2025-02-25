# importa o FastAPI
from fastapi import FastAPI
from router.router import user


# instancia fastapi
app = FastAPI()

app.include_router(user)