let mistakestxt = document.getElementById("mistakes");
let selectedCell;
let mistakes = 0;
let difficulty = ["easy","medium","hard"];
let level = "easy";
let startTime = null;
let interval = null;
let elapsed = 0;

const fetchBoard = async(level_dificulty) => {
    const res = await fetch(`http://127.0.0.1:8000/sudoku_grid/${level_dificulty}`)
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

const startGame = async(level) => {
    const boardGenAndSolution = await fetchBoard(level);
    const board = boardGenAndSolution[0];
    const solution = boardGenAndSolution[1];

    resetClock();
    startClock();
    level = level;
    mistakes = 0;
    document.getElementById('level').innerHTML = `level : ${level}`;
    document.getElementById('mistakes').innerHTML = `mistakes : ${mistakes}`
    document.getElementById('grid').innerHTML = '';
    document.getElementById('selection').innerHTML = '';
    document.getElementById('difficulty').innerHTML = '';


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

    let newGame = document.getElementById("new-game")
    newGame.innerHTML = 'NEW GAME'
    newGame.addEventListener('click',displayDifficulty);
    document.getElementById('difficulty').style.visibility = 'hidden';

    for (let i = 0; i < 3; i+=1) {
        let difficultyButton = document.createElement('div');
        difficultyButton.id = difficulty[i];
        difficultyButton.innerHTML = difficulty[i];
        difficultyButton.classList.add('difficulty-button');
        difficultyButton.addEventListener('click', () => startGame(difficultyButton.id));
        document.getElementById('difficulty').appendChild(difficultyButton)
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
            } else {
                const i = selectedCell.id.charAt(0)
                const j = selectedCell.id.charAt(2)
                if (solution[i][j].value == this.id){
                    selectedCell.classList.remove("wrong-digit")
                    selectedCell.classList.add("correct-digit")
                    if (checkFinish()) {
                        endGame();
                    }
                } else {
                    selectedCell.classList.remove("correct-digit")
                    selectedCell.classList.add("wrong-digit")
                    mistakes += 1
                    document.getElementById('mistakes').innerHTML = `mistakes : ${mistakes}`
                }
            }
        }
    }

    function checkFinish() {
        const cells = document.querySelectorAll("#grid div");
        let allValid = true;
        cells.forEach(cell => {
        if (
            !cell.classList.contains("correct-digit") &&
            !cell.classList.contains("fixed-cell")
        ) {
            allValid = false;
        }
        });
        return allValid;
    }

    function endGame() {
        stopClock();
    }

    async function displayDifficulty() {
        document.getElementById('difficulty').style.visibility = 'visible';
        await new Promise(resolve => setTimeout(resolve, 5000));
        document.getElementById('difficulty').style.visibility = 'hidden';
    }

    async function startClock() {
        if (interval) return;
        startTime = Date.now() - (elapsed || 0);
        interval = setInterval(update, 100);
    }

    async function update() {
        elapsed = Date.now() - startTime;
        let totalSeconds = Math.floor(elapsed / 1000);

        let h = Math.floor(totalSeconds / 3600);
        let m = Math.floor((totalSeconds % 3600) / 60);
        let s = totalSeconds % 60;

        document.getElementById("clock").innerHTML =
            `clock : ${h.toString().padStart(2,"0")}:${m.toString().padStart(2,"0")}:${s.toString().padStart(2,"0")}`;
    }

    async function stopClock() {
        clearInterval(interval);
        interval = null;
    }

    async function resetClock() {
        stopClock();
        elapsed = 0;
    }
}

startGame(level);