"""
Write a function, island_count, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

island_count(grid) # -> 3
grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

island_count(grid) # -> 4
grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

island_count(grid) # -> 1
grid = [
  ['W', 'W'],
  ['W', 'W'],
  ['W', 'W'],
]

island_count(grid) # -> 0
"""

def island_count(grid):
  visited = set()
  count = 0
  
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if (exploreNeighbors(row, col, grid, visited) == True):
        count += 1
  return count
      
def exploreNeighbors(row, col, grid, visited):
  rowBounds = 0 <= row < len(grid)
  colBounds = 0 <= col < len(grid[0])
  print(rowBounds, colBounds)
  if (rowBounds == False or colBounds == False):
    return False
  if (grid[row][col] == 'W'):
    return False

  position = f'{row},{col}'
  if (position in visited):
    return False
  visited.add(position)
  exploreNeighbors(row + 1, col, grid, visited)
  exploreNeighbors(row - 1, col, grid, visited)
  exploreNeighbors(row, col + 1, grid, visited)
  exploreNeighbors(row, col - 1, grid, visited)
  return True