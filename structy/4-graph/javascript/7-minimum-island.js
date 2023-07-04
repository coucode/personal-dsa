/*
Write a function, minimumIsland, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.

const grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
];

minimumIsland(grid); // -> 2
const grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
];

minimumIsland(grid); // -> 1
const grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
];

minimumIsland(grid); // -> 9
const grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
];

minimumIsland(grid); // -> 1
*/
const minimumIsland = (grid) => {
  let smallest = Infinity
  let visited = new Set()

  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[0].length; c++) {
      let size = islandSize(r, c, grid, visited)
      if (size > 0 && size < smallest) {
        smallest = size
      }
    }
  }
  return smallest
};

const islandSize = (r, c, grid, visited) => {
  let rowCheck = r >= 0 && r < grid.length
  let colCheck = c >= 0 && c < grid[0].length

  if (!rowCheck || !colCheck) return 0
  if (grid[r][c] === 'W') return 0

  let position = r + ',' + c

  if (visited.has(position)) return 0
  visited.add(position)

  let count = 1
  count += islandSize(r + 1, c, grid, visited)
  count += islandSize(r - 1, c, grid, visited)
  count += islandSize(r, c + 1, grid, visited)
  count += islandSize(r, c - 1, grid, visited)
  return count
}

