# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        node = root

        while node:
            
            if node.val > val:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    return root
            
            else:
                
                if node.right is not None:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    return root
                
        return root