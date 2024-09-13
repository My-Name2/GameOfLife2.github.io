<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game of Life with Random Colors</title>
    <style>
        canvas {
            border: 1px solid black;
            display: block;
            margin: 0 auto;
        }
        body {
            text-align: center;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <h1>Game of Life with Rainbow Colors</h1>
    <canvas id="gameCanvas"></canvas>

    <script>
        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');
        
        const gridSize = 50;
        const cellSize = 10;
        canvas.width = gridSize * cellSize;
        canvas.height = gridSize * cellSize;

        // Initialize grid and color grid
        let grid = createRandomGrid(gridSize);
        let colorGrid = createColorGrid(gridSize);

        // Create a random color for each cell
        function randomColor() {
            const r = Math.floor(Math.random() * 256);
            const g = Math.floor(Math.random() * 256);
            const b = Math.floor(Math.random() * 256);
            return `rgb(${r},${g},${b})`;
        }

        // Initialize grid with random live/dead cells
        function createRandomGrid(size) {
            let arr = new Array(size).fill(null).map(() => new Array(size).fill(0));
            for (let i = 0; i < size; i++) {
                for (let j = 0; j < size; j++) {
                    arr[i][j] = Math.random() > 0.7 ? 1 : 0;  // 30% chance of alive
                }
            }
            return arr;
        }

        // Initialize color grid
        function createColorGrid(size) {
            let colorGrid = new Array(size).fill(null).map(() => new Array(size).fill('black'));
            return colorGrid;
        }

        // Draw the grid
        function drawGrid(grid, colorGrid) {
            for (let i = 0; i < gridSize; i++) {
                for (let j = 0; j < gridSize; j++) {
                    if (grid[i][j] === 1) {
                        ctx.fillStyle = colorGrid[i][j];  // Use the cell's current color
                    } else {
                        ctx.fillStyle = 'black';  // Dead cells are black
                    }
                    ctx.fillRect(i * cellSize, j * cellSize, cellSize, cellSize);
                }
            }
        }

        // Update grid for each generation based on Conway's rules
        function updateGrid() {
            let newGrid = grid.map(arr => [...arr]);
            for (let i = 0; i < gridSize; i++) {
                for (let j = 0; j < gridSize; j++) {
                    let liveNeighbors = countLiveNeighbors(grid, i, j);
                    
                    if (grid[i][j] === 1) {
                        if (liveNeighbors < 2 || liveNeighbors > 3) {
                            newGrid[i][j] = 0;  // Cell dies
                        }
                    } else {
                        if (liveNeighbors === 3) {
                            newGrid[i][j] = 1;  // Cell becomes alive
                            colorGrid[i][j] = randomColor();  // Assign random color
                        }
                    }
                }
            }
            grid = newGrid;
        }

        // Count live neighbors
        function countLiveNeighbors(grid, x, y) {
            let liveNeighbors = 0;
            for (let i = -1; i <= 1; i++) {
                for (let j = -1; j <= 1; j++) {
                    if (i === 0 && j === 0) continue;  // Skip the current cell
                    const row = (x + i + gridSize) % gridSize;
                    const col = (y + j + gridSize) % gridSize;
                    liveNeighbors += grid[row][col];
                }
            }
            return liveNeighbors;
        }

        // Main game loop
        function gameLoop() {
            updateGrid();
            drawGrid(grid, colorGrid);
            requestAnimationFrame(gameLoop);  // Loop the game continuously
        }

        // Start the game
        gameLoop();
    </script>
</body>
</html>
