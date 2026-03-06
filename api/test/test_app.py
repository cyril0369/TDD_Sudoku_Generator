from api.app import app
from fastapi.testclient import TestClient


def test_index_route():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Generateur de grille de sudoku"}


def test_sudoku_grid_route():
    client = TestClient(app)
    response = client.get("/sudoku_grid/easy")
    assert response.status_code == 200
    data = response.json()
    assert "sudoku" in data
    assert isinstance(data["sudoku"]["grid"]["cells"], list)
    assert 9 == len(data["sudoku"]["grid"]["cells"])


def test_sudoku_solver_route():
    client = TestClient(app)
    sudoku = client.get("/sudoku_grid/easy")
    sudoku_json = sudoku.json()
    response = client.post(
        "/sudoku_solver",
        json=sudoku_json
    )
    assert response.status_code == 200
    data = response.json()
    assert "solution" in data
    assert isinstance(data["solution"]["grid"]["cells"], list)
    assert 9 == len(data["solution"]["grid"]["cells"])
