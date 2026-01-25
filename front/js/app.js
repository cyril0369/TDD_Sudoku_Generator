let mistakestxt = document.getElementById("mistakes");
let selectedDigit;
let mistakes = 0;

const fetchBoard = async() => {
    const res = await fetch('http://127.0.0.1:8000/sudoku_grid/easy')
    if (!res.ok) {
        console.error('HTTP error', res.status);
        return;
    }
    const data = await res.json();
    const board = data["sudoku"]["grid"]["cells"];
    
    console.log(board);
}

const startGame = async() => {
    await fetchBoard();
}

startGame();