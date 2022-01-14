class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here


def reverse(head):
  # Write your code here
  leader = head
  trail = leader
  ls = []
  
  if (not head):
    return []
  
  while leader:
    if (leader.data % 2 == 0):
      ls.append(leader.data)
      leader = leader.next
    else:
      # Reverse
      front = len(ls) - 1
      while(0 <= front):
        trail.data = ls[front]
        front -= 1
        trail = trail.next
      
      ls = []
      if (leader.next):
        leader = leader.next
      trail = leader
      
  if (len(ls) > 0):
    front = len(ls) - 1
    while(0 <= front):
      trail.data = ls[front]
      front -= 1
      trail = trail.next
      
  return head