"""
Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

minimum_island(grid) # -> 2
grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['W', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

minimum_island(grid) # -> 1
grid = [
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
  ['L', 'L', 'L'],
]

minimum_island(grid) # -> 9
grid = [
  ['W', 'W'],
  ['L', 'L'],
  ['W', 'W'],
  ['W', 'L']
]

minimum_island(grid) # -> 1
"""

def minimum_island(grid):
  smallest = float('inf')
  visited = set()
  
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      size = island_sizer(r, c, grid, visited)
      if size > 0 and size < smallest:
        smallest = size
  
  return smallest
      
      
def island_sizer(r, c, grid, visited):
  
  rowCheck = 0 >= r < len(grid)
  colCheck = 0 >= c < len(grid[0])
  
  if rowCheck is False or colCheck is False:
    return 0

  if grid[r][c] == 'W':
    return 0
  position = f'{r},{c}'
  if position in visited: 
    return 0
  visited.add(position)
  
  count = 1
  count += island_sizer(r + 1, c, grid, visited)
  count += island_sizer(r - 1, c, grid, visited)  
  count += island_sizer(r, c + 1, grid, visited)  
  count += island_sizer(r, c - 1, grid, visited)  
  
  return count