/*
Write a function, treeValueCount, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.

const a = new Node(12);
const b = new Node(6);
const c = new Node(6);
const d = new Node(4);
const e = new Node(6);
const f = new Node(12);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      12
//    /   \
//   6     6
//  / \     \
// 4   6     12

treeValueCount(a,  6); // -> 3
const a = new Node(12);
const b = new Node(6);
const c = new Node(6);
const d = new Node(4);
const e = new Node(6);
const f = new Node(12);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;

//      12
//    /   \
//   6     6
//  / \     \
// 4  6     12

treeValueCount(a,  12); // -> 2
const a = new Node(7);
const b = new Node(5);
const c = new Node(1);
const d = new Node(1);
const e = new Node(8);
const f = new Node(7);
const g = new Node(1);
const h = new Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
e.left = g;
f.right = h;

//      7
//    /   \
//   5     1
//  / \     \
// 1   8     7
//    /       \
//   1         1
treeValueCount(a, 1); // -> 4
const a = new Node(7);
const b = new Node(5);
const c = new Node(1);
const d = new Node(1);
const e = new Node(8);
const f = new Node(7);
const g = new Node(1);
const h = new Node(1);

a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
e.left = g;
f.right = h;

//      7
//    /   \
//   5     1
//  / \     \
// 1   8     7
//    /       \
//   1         1

treeValueCount(a, 9); // -> 0
treeValueCount(null, 42); // -> 0
*/
class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

const treeValueCount = (root, target) => {
  if (!root) return 0

  const left = treeValueCount(root.left, target)
  const right = treeValueCount(root.right, target)
  if (root.val === target) {
    return 1 + left + right
  } else {
    return left + right
  }
};
