let isPalindrome = function (s) {
  let string = []
  for (let i = 0; i < s.length; i++) {
    let char = s[i].toLowerCase()
    let alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'
    if (alphanumeric.includes(char)) {
      string.push(char)
    }
  }
  let reversed = [...string].reverse()
  return string.join('') === reversed.join('')
};