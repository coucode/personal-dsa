/*
pair product
Write a function, pairProduct, that takes in an array and a target product as arguments. 
The function should return an array containing a pair of indices whose elements multiply to the given target. 
The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.

pairProduct([3, 2, 5, 4, 1], 8); // -> [1, 3]
pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
pairProduct([4, 7, 9, 2, 5, 1], 5); // -> [4, 5]
pairProduct([4, 7, 9, 2, 5, 1], 35); // -> [1, 4]
pairProduct([3, 2, 5, 4, 1], 10); // -> [1, 2]
pairProduct([4, 6, 8, 2], 16); // -> [2, 3]
*/

/*
ASSUMPTIONS/EDGE CASES:
- Guaranteed to be a pair 
- Indices must be unique

PATTERN: 
- Two Pointer

PSEUDOCODE:
1. Set variables for left, right pointers and answer
2. While answer is false, perform the following steps
3. Iterate through the array
   3a. Multiply the values at the left and right pointer
   3b. If product matches target, return the indices
   3c. If not:
       3c-1: If right pointer is at the end of the array, increment left pointer and set right pointer one indice to the right
       3c-2: Otherwise just increment the right pointer
*/

const pairProduct = (numbers, targetProduct) => {
  let left = 0;
  let right = 1;
  let answer = false;

  while (!answer) {
    if (numbers[left] * numbers[right] === targetProduct) {
      return [left, right]
    } else {
      if (right === numbers.length - 1) {
        left += 1
        right = left + 1
      } else {
        right += 1
      }
    }
  }
};