"""
Write a function, zipper_lists, that takes in the head of two linked lists as 
arguments. The function should zipper the two lists together into single 
linked list by alternating nodes. If one of the linked lists is longer than the 
other, the resulting list should terminate with the remaining nodes. 
The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def zipper_lists(head_1, head_2):
  head = head_1
  tail = head
  curr1 = head_1.next
  curr2 = head_2
  count = 0
  
  while (curr1 is not None and curr2 is not None):
    if count % 2 == 0:
      tail.next = curr2
      curr2 = curr2.next
    else:
      tail.next = curr1
      curr1 = curr1.next
    tail = tail.next
    count +=1
  
  if curr1 is not None: 
    tail.next = curr1
  if curr2 is not None:
    tail.next = curr2
  
  return head