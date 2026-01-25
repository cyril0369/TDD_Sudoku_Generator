from src.generator import generate_suduku


def test_generate_biginer_suduku():
    sudoku = generate_suduku("easy")
    assert 30 <= sudoku.count_zeros() <= 35
