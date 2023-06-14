/*
anagrams
Write a function, anagrams, that takes in two strings as arguments. The function should return a boolean indicating whether or not the strings are anagrams. Anagrams are strings that contain the same characters, but in any order.

anagrams('restful', 'fluster'); // -> true
anagrams('cats', 'tocs'); // -> false
anagrams('monkeyswrite', 'newyorktimes'); // -> true
anagrams('paper', 'reapa'); // -> false
anagrams('elbow', 'below'); // -> true
anagrams('tax', 'taxi'); // -> false
anagrams('taxi', 'tax'); // -> false
anagrams('night', 'thing'); // -> true
anagrams('abbc', 'aabc'); // -> false
anagrams('po', 'popp'); // -> false
anagrams('pp', 'oo') // -> false

*/
// // Solution with Methods
// const anagrams = (s1, s2) => {
//   return s1.split('').sort().join('') == s2.split('').sort().join('')
// };

const anagrams = (s1, s2) => {
  let count = {}

  for (let char1 of s1) {
    if (!count[char1]) {
      count[char1] = 1
    } else {
      count[char1] += 1
    }
  }
  for (let char2 of s2) {
    if (count[char2]) {
      count[char2] -= 1
    } else {
      return false
    }
  }
  for (let char in count) {
    if (count[char] !== 0) {
      return false
    }
  }
  return true
};