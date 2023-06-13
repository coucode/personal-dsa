/*
Write a function, uncompress, that takes in a string as an argument. 
The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.
The function should return an uncompressed version of the string where each 'char' of a group 
is repeated 'number' times consecutively. You may assume that the input string is well-formed 
according to the previously mentioned pattern.

uncompress("2c3a1t"); // -> 'ccaaat'
uncompress("4s2b"); // -> 'ssssbb'
uncompress("2p1o5p"); // -> 'ppoppppp'
uncompress("3n12e2z"); // -> 'nnneeeeeeeeeeeezz'
uncompress("127y"); // ->'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
*/

/*
NOT TWO POINTER ANSWER
*/

// let answer = ''
// let patterns = []
// let num = null
// let char = null

// for (let i = 0; i < s.length; i++) {
//   let current = s[i]
//   let checker = Number(current)
//   if (Number(current)) {
//     if (!num) {
//       num = current
//     } else {
//       num = num + current
//     }
//   } else {
//     char = current
//     patterns.push([Number(num), char])
//     num = null
//     char = null
//   }
// }
// for (let j = 0; j < patterns.length; j++) {
//   let mult = patterns[j][0]
//   let character = patterns[j][1]

//   for (let k = 0; k < mult; k++) {
//     answer = answer + character
//   }
// }
// return answer

const uncompress = (s) => {
  let left = 0;
  let right = 0;
  let answer = '';

  while (right < s.length) {
    let current = s[right]

    if (!Number(current)) {
      let num = Number(s.slice(left, right))
      for (let i = 0; i < num; i++) {
        answer = answer + current
      }
      left = right + 1
      right = left + 1
    } else {
      right++
    }
  }
  return answer
};