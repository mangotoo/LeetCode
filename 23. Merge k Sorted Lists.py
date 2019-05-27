# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        nodes = list()
        
        for linked_list in lists:
            while linked_list:
                nodes.append(linked_list.val)
                linked_list = linked_list.next
        
        if len(nodes) <=0:
            return None
        
        nodes.sort()
        
        root = ListNode(nodes[0])
        prev_node = root
        
        for node in nodes[1:]:
            temp_node = ListNode(node)
            prev_node.next = temp_node
            prev_node = temp_node
            
        return root
            