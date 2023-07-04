/*
Write a function, islandCount, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

const grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
];

islandCount(grid); // -> 3
const grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
];

islandCount(grid); // -> 4
const grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
];

islandCount(grid); // -> 1
 const grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
];

islandCount(grid); // -> 0
*/

const islandCount = (grid) => {
  let count = 0;
  let visited = new Set();

  grid.forEach((row, rowIdx) => {
    row.forEach((col, colIdx) => {
      if (exploreNeighbors(rowIdx, colIdx, grid, visited) === true) {
        count += 1
      }
    })
  })
  return count
};

const exploreNeighbors = function (row, col, grid, visited) {
  const rowBounds = 0 <= row && row < grid.length
  const colBounds = 0 <= col && col < grid[0].length

  if (!rowBounds || !colBounds) return false

  if (grid[row][col] === 'W') return false

  const pos = row + ',' + col
  if (visited.has(pos)) return false
  visited.add(pos)

  exploreNeighbors(row - 1, col, grid, visited);
  exploreNeighbors(row + 1, col, grid, visited);
  exploreNeighbors(row, col - 1, grid, visited);
  exploreNeighbors(row, col + 1, grid, visited);
  return true

}



