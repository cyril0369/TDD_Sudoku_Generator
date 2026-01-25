from fastapi import FastAPI
from src.generator import generate_suduku


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Generateur de grille de sudoku"}


@app.get("/sudoku_grid/{difficulty}")
async def sudoku_grid(difficulty):
    suduku = generate_suduku(difficulty)
    return {"sudoku": suduku}
