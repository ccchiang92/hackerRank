""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def inOrder(node,output):
    if not node.left is None:
        output=inOrder(node.left,output)
    output.append(node.data)
    if not node.right is None:
        output=inOrder(node.right,output)
    return output
def check_binary_search_tree_(root):
    if root is None:
        return True
    else:
        order = inOrder(root,[])
        return order==sorted(order) and list(set(order))==order
        