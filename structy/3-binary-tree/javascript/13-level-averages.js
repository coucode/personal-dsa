/*
Write a function, levelAverages, that takes in the root of a binary tree that contains number values. The function should return an array containing the average value of each level.

const a = new Node(3);
const b = new Node(11);
const c = new Node(4);
const d = new Node(4);
const e = new Node(-2);
const f = new Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//       3
//    /    \
//   11     4
//  / \      \
// 4   -2     1

levelAverages(a); // -> [ 3, 7.5, 1 ] 
const a = new Node(5);
const b = new Node(11);
const c = new Node(54);
const d = new Node(20);
const e = new Node(15);
const f = new Node(1);
const g = new Node(3);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
e.left = f;
e.right = g;

//        5
//     /    \
//    11    54
//  /   \
// 20   15
//      / \
//     1  3

levelAverages(a); // -> [ 5, 32.5, 17.5, 2 ] 
const a = new Node(-1);
const b = new Node(-6);
const c = new Node(-5);
const d = new Node(-3);
const e = new Node(0);
const f = new Node(45);
const g = new Node(-1);
const h = new Node(-2);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
e.left = g;
f.right = h;

//        -1
//      /   \
//    -6    -5
//   /  \     \
// -3   0     45
//     /       \
//    -1       -2

levelAverages(a); // -> [ -1, -5.5, 14, -1.5 ]
const q = new Node(13);
const r = new Node(4);
const s = new Node(2);
const t = new Node(9);
const u = new Node(2);
const v = new Node(42);

q.left = r;
q.right = s;
r.right = t;
t.left = u;
u.right = v;

//        13
//      /   \
//     4     2
//      \
//       9
//      /
//     2
//    /
//   42

levelAverages(q); // -> [ 13, 3, 9, 2, 42 ]
levelAverages(null); // -> [ ]
*/
class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const levelAverages = (root) => {
  if (!root) return []

  let levels = []
  let queue = [{ node: root, levelNum: 0 }]

  while (queue.length > 0) {
    const { node, levelNum } = queue.shift()

    if (levels.length === levelNum) {
      levels[levelNum] = { sum: node.val, count: 1 }
    } else {
      levels[levelNum] = { sum: levels[levelNum].sum + node.val, count: levels[levelNum].count + 1 }
    }
    if (node.left) queue.push({ node: node.left, levelNum: levelNum + 1 })
    if (node.right) queue.push({ node: node.right, levelNum: levelNum + 1 })
  }
  levels.forEach((level, idx) => {
    let average = level.sum / level.count
    levels[idx] = average
  })
  return levels

};