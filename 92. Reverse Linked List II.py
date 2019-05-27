# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prev_node = None
        current_node = head
        
        while m > 1:
            prev_node = current_node
            current_node = current_node.next
            m-=1
            n-=1
        
        before_reversal = prev_node
        tail = current_node
        prev_node = None
        
        while n > 0:
            temp_next = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = temp_next
            n-=1
            
        if before_reversal is None:
            head = prev_node
        else:
            before_reversal.next = prev_node

        tail.next = current_node
        
        return head