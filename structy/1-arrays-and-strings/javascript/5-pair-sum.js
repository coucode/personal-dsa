/*
pair sum
Write a function, pairSum, that takes in an array and a target sum as arguments. 
The function should return an array containing a pair of indices whose elements sum to the given target.
The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.

pairSum([3, 2, 5, 4, 1], 8); // -> [0, 2]
pairSum([4, 7, 9, 2, 5, 1], 5); // -> [0, 5]
pairSum([4, 7, 9, 2, 5, 1], 3); // -> [3, 5]
pairSum([1, 6, 7, 2], 13); // -> [1, 2]
pairSum([9, 9], 18); // -> [0, 1]
pairSum([6, 4, 2, 8 ], 12); // -> [1, 3]
*/


const pairSum = (numbers, targetSum) => {
  let left = 0
  let right = 1
  let answer = false

  while (!answer) {
    if (numbers[left] + numbers[right] === targetSum) {
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