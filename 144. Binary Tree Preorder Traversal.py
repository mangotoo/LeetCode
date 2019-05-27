# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def preorder(self, root, values):
        values.append(root.val)
        
        if root.left is not None:
            self.preorder(root.left, values)
        
        if root.right is not None:
            self.preorder(root.right, values)
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        values = list()
        
        if root is None:
            return values
        
        self.preorder(root, values)
        
        return values