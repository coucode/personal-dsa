/*
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
*/
var isValid = function (s) {
  // Assumptions
  // String has odd length, it is automatically false

  // Edge Cases
  // [(]) this is FALSE
  // {[]} this is TRUE
  // if (s.length % 2 !== 0) return false
  let stack = []
  let obj = {
    ")": "(",
    "]": "[",
    "}": "{"
  }
  for (let i = 0; i < s.length; i++) {
    let char = s[i]
    if (char === "(" || char === "[" || char === "{") {
      stack.push(char)
    }
    if (char === ")") {
      if (stack[stack.length - 1] === obj[")"]) {
        stack.pop()
      } else {
        return false
      }
    }
    if (char === "]") {
      if (stack[stack.length - 1] === obj["]"]) {
        stack.pop()
      } else {
        return false
      }
    }
    if (char === "}") {
      if (stack[stack.length - 1] === obj["}"]) {
        stack.pop()
      } else {
        return false
      }
    }

  }
  if (stack.length) return false
  return true
};