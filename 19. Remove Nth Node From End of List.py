# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        head_runner = head
        trail_runner = head
        
        while n>1:
            head_runner = head_runner.next
            n-=1
            
        prev_node = None
        
        while head_runner.next:
            head_runner = head_runner.next
            prev_node = trail_runner
            trail_runner = trail_runner.next
            
        if prev_node is not None:
            prev_node.next = trail_runner.next
            return head
        
        else:
            return head.next
