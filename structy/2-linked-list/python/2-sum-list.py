"""
sum list
Write a function, sumList, that takes in the head of a linked list containing 
numbers as an argument. The function should return the total sum of all values in the linked list.

const a = new Node(2);
const b = new Node(8);
const c = new Node(3);
const d = new Node(-1);
const e = new Node(7);

a.next = b;
b.next = c;
c.next = d;
d.next = e;

// 2 -> 8 -> 3 -> -1 -> 7

sumList(a); // 19
const x = new Node(38);
const y = new Node(4);

x.next = y;

// 38 -> 4

sumList(x); // 42
const z = new Node(100);

// 100

sumList(z); // 100
sumList(null); // 0
"""
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def sum_list(head):
  sum = 0
  current = head
  
  while current is not None:
    sum += current.val
    current = current.next
  return sum