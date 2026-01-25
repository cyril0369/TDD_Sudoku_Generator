from src.generator import generate_suduku, generate_sudoku_from_json
from src.sudoku import Sudoku

json = {
    "sudoku": {
        "grid": {
            "cells": [
                [
                    {
                        "value": 4
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 2
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 5
                    }
                ],
                [
                    {
                        "value": 7
                    },
                    {
                        "value": 5
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 3
                    },
                    {
                        "value": 9
                    },
                    {
                        "value": 8
                    },
                    {
                        "value": 4
                    },
                    {
                        "value": 2
                    },
                    {
                        "value": 0
                    }
                ],
                [
                    {
                        "value": 2
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 4
                    },
                    {
                        "value": 6
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 3
                    },
                    {
                        "value": 7
                    },
                    {
                        "value": 0
                    }
                ],
                [
                    {
                        "value": 8
                    },
                    {
                        "value": 4
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 3
                    },
                    {
                        "value": 9
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    }
                ],
                [
                    {
                        "value": 1
                    },
                    {
                        "value": 6
                    },
                    {
                        "value": 3
                    },
                    {
                        "value": 8
                    },
                    {
                        "value": 5
                    },
                    {
                        "value": 2
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    }
                ],
                [
                    {
                        "value": 9
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 2
                    },
                    {
                        "value": 6
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 5
                    },
                    {
                        "value": 3
                    },
                    {
                        "value": 0
                    }
                ],
                [
                    {
                        "value": 3
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 9
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 7
                    },
                    {
                        "value": 6
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 4
                    }
                ],
                [
                    {
                        "value": 5
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 7
                    },
                    {
                        "value": 1
                    },
                    {
                        "value": 2
                    },
                    {
                        "value": 4
                    },
                    {
                        "value": 6
                    },
                    {
                        "value": 9
                    },
                    {
                        "value": 3
                    }
                ],
                [
                    {
                        "value": 0
                    },
                    {
                        "value": 1
                    },
                    {
                        "value": 4
                    },
                    {
                        "value": 9
                    },
                    {
                        "value": 0
                    },
                    {
                        "value": 3
                    },
                    {
                        "value": 2
                    },
                    {
                        "value": 5
                    },
                    {
                        "value": 7
                    }
                ]
            ]
        }
    }
}


def test_generate_biginer_suduku():
    sudoku = generate_suduku("easy")
    assert 30 <= sudoku.count_zeros() <= 35


def test_generate_sudoku_from_json():
    sudoku_from_json = generate_sudoku_from_json(json)
    assert isinstance(sudoku_from_json, Sudoku)
    assert 4 == sudoku_from_json.grid.cells[0][0].value
