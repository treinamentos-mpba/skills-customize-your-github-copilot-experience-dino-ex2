from fastapi import FastAPI

app = FastAPI()

# Lista em memória usada como "banco de dados" da API
items = [
    {"id": 1, "name": "Caderno", "price": 12.5},
    {"id": 2, "name": "Caneta", "price": 3.0},
]

# Salve como main.py e execute com: uvicorn main:app --reload
# Depois acesse http://127.0.0.1:8000/docs
