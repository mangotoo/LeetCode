# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    def reverseList(self, head):
        
        current_node = head
        prev_node = None
        
        while current_node is not None:
            
            temp_next = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp_next
        
        return prev_node
    
    def spliceLists(self, list_1, list_2, flag):
        
        if list_1:
            return list_2
        
        elif list_2:
            return list_1
        
        elif flag:
            list_1.next = self.spliceLists(list_1.next, list_2, False)
            return list_1
        
        else:
            list_2.next = self.spliceLists(list_1, list_2.next, True)
            return list_2
    
    def splitList(self, head):
        
        slow_runner = head
        fast_runner = head
        prev_node = None
        
        while fast_runner is not None and fast_runner.next is not None:
            prev_node = slow_runner
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
        
        if prev_node is not None:
            prev_node.next = None
        
        return (head, slow_runner)
        
  
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        if head is None or head.next is None:
            return head
        
        else:
            
            list_1, list_2 = self.splitList(head)
            list_2 = self.reverseList(list_2)
            head = self.spliceLists(list_1, list_2, True)
            
        