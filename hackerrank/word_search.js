/*
Given an m x n grid of characters board and a string word, return true if word exists in the grid 
*/

function neighborCheck(board, row, col, char, used) {
  // Above
  let above = row - 1
  let left = col - 1
  let below = row + 1
  let right = col + 1
  console.log("CHAR", char)

  if (above > 0 && used.has(`${above},${col}`) === false && board[above][col].toUpperCase() === char.toUpperCase()) {
    return [above, col]
  }
  // Below
  else if (below < board.length && used.has(`${below},${col}`) === false && board[below][col].toUpperCase() === char.toUpperCase()) {
    return [below, col]
  }
  // Left
  else if (left >= 0 && used.has(`${row},${left}`) === false && board[row][left].toUpperCase() === char.toUpperCase()) {
    return [row, left]
  }
  // Right
  else if (right < board[0].length && used.has(`${row},${right}`) === false && board[row][right].toUpperCase() === char.toUpperCase()) {
    return [row, right]
  } else {
    return false
  }


}

function exist(board, word) {

  for (let row = 0; row < board.length; row++) {
    for (let col = 0; col < board[row].length; col++) {
      if (board[row][col].toUpperCase() === word[0].toUpperCase()) {
        let used = new Set
        used.add(`${row},${col}`)
        let wordIndex = 1
        let wordDupe = word[0]
        // Checks neighbors
        let current = [row, col]
        while (wordIndex <= word.length) {
          console.log("CURRENT", current)
          console.log("USED", used)
          console.log("ee", word.length, wordIndex, word[wordIndex])
          console.log(wordDupe, word)
          if (wordDupe === word) {
            return true
          }
          let present = neighborCheck(board, current[0], current[1], word[wordIndex], used)
          console.log("PRESENT", present)
          if (present === false) {
            console.log("NOT PRESENT")
            break
          } else {
            wordIndex += 1
            current = [present[0], present[1]]
            wordDupe = wordDupe + board[present[0]][present[1]]
            used.add(`${present[0]}, ${present[1]}`)
          }

        }
      }
    }
  }
  return false
}