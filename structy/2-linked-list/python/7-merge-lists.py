"""
Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. 
The function should merge the two lists together into single sorted linked list. The function 
should return the head of the merged linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty and contain increasing sorted numbers.
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  head = None
  curr1 = head_1
  curr2 = head_2
  if head_1.val < head_2.val:
    head = curr1
    curr1 = curr1.next
  else:
    head = curr2
    curr2 = curr2.next
  tail = head
  
  while (curr1 is not None and curr2 is not None):
    if curr1.val < curr2.val:
      tail.next = curr1
      curr1 = curr1.next
    else: 
      tail.next = curr2
      curr2 = curr2.next
    tail = tail.next
  if curr1 is not None:
    tail.next = curr1
  if curr2 is not None:
    tail.next = curr2
    
  return head