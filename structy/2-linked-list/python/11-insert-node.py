"""
Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

Do this in-place.

You may assume that the input list is non-empty and the index is not greater than the length of the input list.

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, 'x', 2)
# a -> b -> x -> c -> d
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, 'v', 3)
# a -> b -> c -> v -> d
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

insert_node(a, 'm', 4)
# a -> b -> c -> d -> m
a = Node("a")
b = Node("b")

a.next = b

# a -> b

insert_node(a, 'z', 0)
# z -> a -> b
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  curr = head
  new_node = Node(value)
  curr_index = 0
  prev = None
  
  if curr_index == index:
    new_node.next = curr
    return new_node
  
  answer = head
  
  while curr is not None:
    if curr_index + 1 == index:
      new_node.next = curr.next
      curr.next = new_node
    curr = curr.next
    curr_index += 1
    
  return answer