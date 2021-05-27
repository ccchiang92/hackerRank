""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    def recursiveCheck(node, maximum, minimum):
        if node is None:
            return True
        else:
            return node.data>minimum and node.data<maximum and recursiveCheck(node.left,node.data,minimum) and recursiveCheck(node.right,maximum,node.data)
    return recursiveCheck(root,10001,-1)