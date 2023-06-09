/*
Write a function, zipperLists, that takes in the head of two linked lists as arguments. 
The function should zipper the two lists together into single linked list by alternating nodes. 
If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. 

The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.
*/

class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

const zipperLists = (head1, head2) => {
  const head = head1
  let tail = head
  let curr1 = head1.next
  let curr2 = head2
  let count = 0;

  while (curr1 !== null && curr2 !== null) {
    if (count % 2 === 0) {
      tail.next = curr2
      curr2 = curr2.next
    } else {
      tail.next = curr1
      curr1 = curr1.next
    }
    tail = tail.next
    count++
  }
  if (curr1 !== null) tail.next = curr1
  if (curr2 !== null) tail.next = curr2

  return head
};