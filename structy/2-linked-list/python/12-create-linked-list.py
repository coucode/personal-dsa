"""
Write a function, create_linked_list, that takes in a list of values as an argument. 
The function should create a linked list containing each item of the list as the values 
of the nodes. The function should return the head of the linked list.

create_linked_list(["h", "e", "y"])
# h -> e -> y
create_linked_list([1, 7, 1, 8])
# 1 -> 7 -> 1 -> 8
create_linked_list(["a"])
# a
create_linked_list([])
# null
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  if len(values) == 0:
    return None
  
  head = None
  curr = None
  
  for idx, value in enumerate(values):
    if idx == 0:
      head = Node(value)
      curr = head
    else:
      curr.next = Node(value)
      curr = curr.next
  return head