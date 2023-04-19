/*
HackerRank 4/24/23
True Stack? 

Given two integer arrays pushed and popped each with distinct values, 
return true if this could have been the result of a sequence of push and pop
operations on an initially empty stack, or false otherwise

Example 1: 
Input: pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]
Output: true
Explanation: We might do the following sequence: 
push(1), push(2), push(3), push(4)
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2: 
Input: pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]
Output: false
Explanation: 1 cannot be popped before 2

Constraints: 
- 1 <= pushed.length <= 1000
- 0 <= pushed[i] <= 1000
- All the elements of pushed are unique
- popped.length == pushed.length
- popped is a permutation of pushed
*/

/*
 * Complete the 'real_stack' function below.
 *
 * The function is expected to return a BOOLEAN.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY pushed
 *  2. INTEGER_ARRAY popped
 */

function real_stack(pushed, popped) {
  let seq = pushed.indexOf(popped[0])
  let stack = pushed.slice(0, seq + 1)
  pushed = pushed.slice(seq + 1)

  while (pushed.length || popped.length) {
    if (popped[0] === stack[stack.length - 1]) {
      popped.shift()
      stack.pop()
    } else if (pushed.indexOf(popped[0]) !== -1) {
      stack.push(pushed.shift())
    } else {
      return false
    }
  }
  return true
}