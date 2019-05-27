"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        node_map = {}
        current_node = head
        prev_copy = None
        
        if head is None:
            return None
                
        while current_node is not None:
            current_val = current_node.val
            current_copy = Node(current_val, None, None)
            node_map[current_node] = current_copy
            
            if prev_copy is not None:
                prev_copy.next = current_copy
            
            prev_copy = current_copy
            
            temp_next = current_node.next
            current_node = temp_next
            
        
        for key in node_map.keys():
            original_node = key
            copied_node = node_map[key]
            
            if original_node.random is not None:
                copied_node.random = node_map[original_node.random]
            else:
                copied_node.random = None
        
        return node_map[head]
            
            
            
            
            
            
        
        