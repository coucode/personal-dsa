/*
most frequent char
Write a function, mostFrequentChar, that takes in a string as an argument. 
The function should return the most frequent character of the string. 
If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.

mostFrequentChar('bookeeper'); // -> 'e'
mostFrequentChar('david'); // -> 'd'
mostFrequentChar('abby'); // -> 'b'
mostFrequentChar('mississippi'); // -> 'i'
mostFrequentChar('potato'); // -> 'o'
mostFrequentChar('eleventennine'); // -> 'e'
mostFrequentChar("riverbed"); // -> 'r'
*/

/*
ASSUMPTIONS/EDGE CASES: 
- string is non-empty
- will all characters be in the same case? 
- must return the character that appears earlier in the string 

PSEUDOCODE: 
1. Create an object that keeps count of each character
2. Create a variable that holds the highest value
3. Create a variable that holds the character with the highest value 
4. Iterate backward through the string:
   4a. If the character does not exist in the object, add it to the object with a value of 1
   4b. If the character exists: 
       4b-1. Increment the value associated with the character
       4b-2. Check if that value is greater or equal than the variable holding the max value
             4b-2a. If it is, set the max value to this char's value
             4b-2b. Set the character to this char's value
5. Return the variable holding the character
*/

const mostFrequentChar = (s) => {
  let counter = {}
  let max = 0;
  let char = '';

  for (let i = s.length - 1; i >= 0; i--) {
    let current = s[i]

    if (!counter[current]) {
      counter[current] = 1
    } else {
      counter[current] += 1

      if (counter[current] >= max) {
        max = counter[current]
        char = current
      }
    }
  }
  return char
};
