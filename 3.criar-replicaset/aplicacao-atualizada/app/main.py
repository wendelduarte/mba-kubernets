from fastapi import FastAPI
import os

HOSTNAME = os.environ["HOSTNAME"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": f"Estou rodando dentro de um pod Kubernetes de nome {HOSTNAME} e sou uma versão atualizada..."}

@app.get("/variaveis_de_ambiente")
async def variaveis_de_ambiente():
    return {
        "hostname": HOSTNAME,
        "username": USERNAME,
        "password": PASSWORD
        }