"""
Write a function, add_lists, that takes in the head of two linked lists, each representing a number. The nodes of the linked lists contain digits as values. The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

You must do this by traversing through the linked lists once.

Say we wanted to compute 621 + 354 normally. The sum is 975:

   621
 + 354
 -----
   975

Then, the reversed linked list format of this problem would appear as:

    1 -> 2 -> 6
 +  4 -> 5 -> 3
 --------------
    5 -> 7 -> 9
#   621
# + 354
# -----
#   975

a1 = Node(1)
a2 = Node(2)
a3 = Node(6)
a1.next = a2
a2.next = a3
# 1 -> 2 -> 6

b1 = Node(4)
b2 = Node(5)
b3 = Node(3)
b1.next = b2
b2.next = b3
# 4 -> 5 -> 3

add_lists(a1, b1)
# 5 -> 7 -> 9
#  7541
# +  32
# -----
#  7573

a1 = Node(1)
a2 = Node(4)
a3 = Node(5)
a4 = Node(7)
a1.next = a2
a2.next = a3
a3.next = a4
# 1 -> 4 -> 5 -> 7

b1 = Node(2)
b2 = Node(3)
b1.next = b2
# 2 -> 3 

add_lists(a1, b1)
# 3 -> 7 -> 5 -> 7
#   39
# + 47
# ----
#   86

a1 = Node(9)
a2 = Node(3)
a1.next = a2
# 9 -> 3

b1 = Node(7)
b2 = Node(4)
b1.next = b2
# 7 -> 4

add_lists(a1, b1)
# 6 -> 8
#   89
# + 47
# ----
#  136

a1 = Node(9)
a2 = Node(8)
a1.next = a2
# 9 -> 8

b1 = Node(7)
b2 = Node(4)
b1.next = b2
# 7 -> 4

add_lists(a1, b1)
# 6 -> 3 -> 1
#   999
#  +  6
#  ----
#  1005

a1 = Node(9)
a2 = Node(9)
a3 = Node(9)
a1.next = a2
a2.next = a3
# 9 -> 9 -> 9

b1 = Node(6)
# 6

add_lists(a1, b1)
# 5 -> 0 -> 0 -> 1
"""

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  curr1 = head_1
  num1_string = ''
  
  while curr1 is not None:
    num1_string = str(curr1.val) + num1_string
    curr1 = curr1.next
  
  curr2 = head_2
  num2_string = ''
  
  while curr2 is not None:
    num2_string = str(curr2.val) + num2_string
    curr2 = curr2.next
  
  sum = int(num1_string) + int(num2_string)
  sum = str(sum)
  
  curr = None
  
  for digit in sum:
    node = Node(digit)
    
    if curr is None:
      curr = node
    else: 
      node.next = curr
      curr = node
  return curr