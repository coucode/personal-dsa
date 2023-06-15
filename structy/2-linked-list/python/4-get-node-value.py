"""
get node value
Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None.

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 2) # 'c'
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 3) # 'd'
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

get_node_value(a, 7) # None
node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

get_node_value(node1, 0) # 'banana'
node1 = Node("banana")
node2 = Node("mango")

node1.next = node2

# banana -> mango

get_node_value(node1, 1) # 'mango'
"""
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def get_node_value(head, index):
  curIndex = 0
  current = head
  
  while current is not None:
    if index == curIndex:
      return current.val
    current = current.next
    curIndex +=1
  return None