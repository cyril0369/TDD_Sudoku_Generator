from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.generator import generate_suduku


app = FastAPI()

origins = [
    "http://127.0.0.1:8080",  # l'adresse de ton front
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Generateur de grille de sudoku"}


@app.get("/sudoku_grid/{difficulty}")
async def sudoku_grid(difficulty):
    suduku = generate_suduku(difficulty)
    return {"sudoku": suduku}
