# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is not None and head.next is not None:
            slow_runner = head.next
            fast_runner = head.next.next
        else:
            return None
        
        while fast_runner != slow_runner:
            
            if fast_runner is None or fast_runner.next is None:
                return None
            
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
            
        new_runner = head
        
        while new_runner != slow_runner:
            new_runner = new_runner.next
            slow_runner = slow_runner.next
            
        return new_runner