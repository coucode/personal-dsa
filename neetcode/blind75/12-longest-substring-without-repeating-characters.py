/**
 * @param {string} s
 * @return {number}
 */
let lengthOfLongestSubstring = function(s) {
   let table = {}
   let maxCount = 0;
   if (s.length === 0) return 0

   for (let i = 0; i < s.length; i++){
       let count = 0;
       let str = s[i]
       for (let j = i + 1; j < s.length; j++){
           if (str.indexOf(s[j]) === -1){
               str = str + s[j]
               count++
               table[count] = str
               maxCount = Math.max(count, maxCount)
           } else {
               break
           }
       }
   }
   return maxCount + 1
};