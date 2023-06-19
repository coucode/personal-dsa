/*
create linked list
Write a function, createLinkedList, that takes in an array of values as an argument. The function should create a linked list containing each element of the array as the values of the nodes. The function should return the head of the linked list.

createLinkedList(["h", "e", "y"]);
// h -> e -> y
createLinkedList([1, 7, 1, 8]);
// 1 -> 7 -> 1 -> 8
createLinkedList(["a"]);
// a
createLinkedList([]);
// null
*/
class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const createLinkedList = (values) => {
  let head = null
  let current;

  for (let i = 0; i < values.length; i++) {
    let newNode = new Node(values[i])
    if (i === 0) {
      head = newNode
      current = head
    } else {
      current.next = newNode
      current = current.next
    }
  }
  return head
}