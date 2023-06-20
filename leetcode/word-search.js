/*
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
*/


const isOutOfBound = (board, row, col) => row < 0 || row >= board.length || col < 0 || col >= board[0].length;

const checkNeighbors = (board, word, row, col) => {
  if (!word.length) return true
  if (isOutOfBound(board, row, col) || board[row][col] !== word[0]) return false

  const curr = board[row][col]
  const newWord = word.substring(1)

  board[row][col] = 0;

  const results = checkNeighbors(board, newWord, row + 1, col) ||
    checkNeighbors(board, newWord, row - 1, col) ||
    checkNeighbors(board, newWord, row, col - 1) ||
    checkNeighbors(board, newWord, row, col + 1)

  board[row][col] = curr
  return results
}

let exist = function (board, word) {
  for (let row = 0; row < board.length; row++) {
    for (let col = 0; col < board[row].length; col++) {
      if (checkNeighbors(board, word, row, col)) return true
    }
  }
  return false
};