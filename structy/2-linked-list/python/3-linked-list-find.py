"""
Write a function, linked_list_find, that takes in the head of a linked list and a target value. The function should return a boolean indicating whether or not the linked list contains the target.

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "c") # True
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "d") # True
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")

a.next = b
b.next = c
c.next = d

# a -> b -> c -> d

linked_list_find(a, "q") # False
node1 = Node("jason")
node2 = Node("leneli")

node1.next = node2

# jason -> leneli

linked_list_find(node1, "jason") # True
node1 = Node(42)

# 42

linked_list_find(node1, 42) # True
node1 = Node(42)

# 42

linked_list_find(node1, 100) # False
"""

# Recursive Solution
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def linked_list_find(head, target):
  current = head
  
  if current is None:
    return False
  if current.val == target:
    return True
  current = current.next
  return linked_list_find(current, target)