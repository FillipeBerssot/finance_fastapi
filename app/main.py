from fastapi import FastAPI
from app.core.config import settings


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

@app.get("/")
def root():
    return {"message": "Olá, seja-vindo à Finance API!", "status": "active"}


@app.get("/teste")
def teste_rota():
    return {"teste": "ok"}