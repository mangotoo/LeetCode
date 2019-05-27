"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        clone_map = {}
        clone_map[node] = Node(node.val, [])
        queue = deque([node])
        
        while queue:
            current_node = queue.pop()
            
            for neighbor in current_node.neighbors:
                
                if neighbor not in clone_map:
                    clone = Node(neighbor.val, [])
                    clone_map[neighbor] = clone
                    queue.appendleft(neighbor)
                
                clone_map[current_node].neighbors.append(clone_map[neighbor])
        
        return clone_map[node]