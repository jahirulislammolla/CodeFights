#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(root, s):
    if root==None:
        return s==0
    if root.left==None and root.right==None:
        return s==root.value
    s-=root.value
    if root.left and hasPathWithGivenSum(root.left, s):
        return True
    if root.right and hasPathWithGivenSum(root.right, s):
        return True
    return False
    
