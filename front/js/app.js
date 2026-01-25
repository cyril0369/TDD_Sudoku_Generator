let mistakestxt = document.getElementById("mistakes");
let selectedCell;
let mistakes = 0;

const fetchBoard = async() => {
    const res = await fetch('http://127.0.0.1:8000/sudoku_grid/hard')
    if (!res.ok) {
        console.error('HTTP error', res.status);
        return;
    }
    const data = await res.json();
    const board = data["sudoku"]["grid"]["cells"];

    const fetchSolution = await fetch('http://127.0.0.1:8000/sudoku_solver', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {'Content-Type': 'application/json'}
    })

    const solution = await fetchSolution.json();
    const boardSolution = solution["solution"]["grid"]["cells"]

    return [board, boardSolution]
}

const startGame = async() => {
    const boardGenAndSolution = await fetchBoard();
    const board = boardGenAndSolution[0];
    const solution = boardGenAndSolution[1];

    console.log(board, solution)

    for (let i = 0; i <= 9; i+=1) {
        let digit = document.createElement('div');
        digit.id = i;
        digit.innerHTML = i;
        digit.addEventListener('click', writeDigit)
        digit.classList.add('digit');
        document.getElementById('selection').appendChild(digit);
    }

    for (let row = 0; row < 9; row += 1) {
        for (let column = 0; column < 9; column += 1) {
            let cell = document.createElement('div');
            cell.id = row+'-'+column;
            if (board[row][column]["value"] != 0 ) {
                cell.innerHTML = board[row][column]["value"];
                cell.classList.add('fixed-cell');
            } 
            else {
                cell.classList.add('unfixed-cell');
                cell.addEventListener('click', setCell)
            }
            if (row == 2 || row == 5 ) cell.classList.add('cell-bottum-border');
            if (column == 2 || column == 5) cell.classList.add('cell-right-border');
            cell.classList.add('cell');
            document.getElementById('grid').append(cell);
        }
    }

    function setCell() {
        if (selectedCell != undefined) selectedCell.classList.remove("selected-cell")
        selectedCell = this;
        selectedCell.classList.add("selected-cell")
    }
    
    function writeDigit() {
        if (selectedCell != undefined) {
            selectedCell.innerHTML = this.innerHTML;
            if (this.id == 0){
                selectedCell.classList.remove("wrong-digit");
                selectedCell.classList.remove("correct-digit");
                selectedCell.innerHTML = '';
            }
            const i = selectedCell.id.charAt(0)
            const j = selectedCell.id.charAt(2)
            if (solution[i][j].value == this.id){
                selectedCell.classList.remove("wrong-digit")
                selectedCell.classList.add("correct-digit")
            } else {
                selectedCell.classList.remove("correct-digit")
                selectedCell.classList.add("wrong-digit")
            }
        }
    }
}

startGame();