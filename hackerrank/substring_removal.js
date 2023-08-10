/*
Substring Removal

Given a string seq consisting of the characters 'A' and 'B' only, in one move, 
you can delete either an "AB" or "BB" substring. 
After a move, the remaining parts of the string get concatenated 

Find the minimum possible length of the remaining string after performing any number of moves. 

Note - A substring is a contiguous subsequence of a string

Example: 
seq = "BABBA"

Using 0-based indexing, the followign moves are optimal. 

- Delete the substring "AB" starting at index 1 "BABBA" --> "BBA"
- Delete the substring "BB" starting at index 0 "BBA" --> "A"

There are no more moves so the minumum prossible length of the remaining string is 1. 



*/

/*
 * Complete the 'getMinLength' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING seq as parameter.
 */

function getMinLength(seq) {
  let index = true
  while (index >= 0) {
    if (seq.indexOf("AB") !== -1) {
      // console.log("AB")
      index = seq.indexOf("AB")
    } else if (seq.indexOf("BB") !== -1) {
      // console.log("BB")
      index = seq.indexOf("BB")
    } else {
      // console.log("FALSE")
      index = -1
    }
    // console.log(seq, index)
    if (index >= 0) {
      let start = seq.slice(0, index)
      let end = seq.slice(index + 2)
      // console.log(start, end)
      seq = start + end
    }
    // console.log(seq)

  }
  return seq.length
}
