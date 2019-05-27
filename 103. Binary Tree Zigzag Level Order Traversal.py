# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def levelTraversal(self, node, level, levels):
        
        if level > len(levels) - 1:
            levels.append([node.val])
        
        else:
            levels[level].append(node.val)
            
        if node.left is not None:
            self.levelTraversal(node.left, level+1, levels)
            
        if node.right is not None:
            self.levelTraversal(node.right, level+1, levels)
    
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if root is not None:
            self.levelTraversal(root, 0, levels)
            
            level_count = 1
            
            for level in levels:
                if not level_count%2:
                    level.reverse()
                level_count+=1
                
            return levels
                
        else:
            return levels
            
        