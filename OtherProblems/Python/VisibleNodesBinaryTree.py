class TreeNode: 
  def __init__(self,key): 
    self.left = None
    self.right = None
    self.val = key 

# Add any helper functions you may need here
def traverse(node, level, maxval):
  if (level > maxval):
    maxval = level
  
  if (node.left):
    left = traverse(node.left, level + 1, maxval)
    if (left > maxval):
      maxval = left
  if (node.right):
    right = traverse(node.right, level + 1, maxval)
    if (right > maxval):
      maxval = right
  return maxval

def visible_nodes(root):
  # Write your code here
  level = 1
  maxval = level
  if (root.left):
    left = traverse(root.left, level + 1, maxval)
    if (left > maxval):
      maxval = left
  if (root.right):
    right = traverse(root.right, level + 1, maxval)
    if (right > maxval):
      maxval = right
    
  return maxval