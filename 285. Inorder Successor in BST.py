# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, node, values):
        
        if node.left is not None:
            self.inorderTraversal(node.left, values)
            
        values.append(node)
        
        if node.right is not None:
            self.inorderTraversal(node.right, values)
        
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        prev_node = None
        current_node = root
        
        while current_node:
            if current_node.val > p.val:
                prev_node = current_node
                current_node = current_node.left
            
            else:
                current_node = current_node.right
                
        return prev_node