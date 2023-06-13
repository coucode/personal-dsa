/*
Write a function, compress, that takes in a string as an argument.
The function should return a compressed version of the string where consecutive 
ccurrences of the same characters are compressed into the number of occurrences 
followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'
You can assume that the input only contains alphabetic characters.
*/

const compress = (s) => {
  let left = right = 0;
  let answer = ''
  s += '!'
  while (right < s.length) {
    if (s[left] == s[right]) {
      right++
    } else {
      let count = right - left
      if (count === 1) {
        answer = answer + s[left]
      } else {
        answer = answer + count + s[left]
      }
      left = right
    }
  }

  return answer
};