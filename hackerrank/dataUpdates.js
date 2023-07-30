/*
 * Complete the 'getFinalData' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY data
 *  2. 2D_INTEGER_ARRAY updates
 */

/*
ASSUMPTIONS: 
- 
EDGE CASES: 

PSEUDOCODE: 


*/

function getFinalData(data, updates) {
  for (let update of updates) {
    let start = update[0] - 1
    let end = update[1] - 1

    while (start <= end) {
      data[start] = data[start] * -1
      start++
    }
  }
  return data
}