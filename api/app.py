from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.generator import generate_suduku, generate_sudoku_from_json


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


@app.post("/sudoku_solver")
async def sudoku_solver(sudoku_json: dict):
    sudoku = generate_sudoku_from_json(sudoku_json)
    sudoku.is_valid(0)
    return {"solution": sudoku}
