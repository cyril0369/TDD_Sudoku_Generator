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
