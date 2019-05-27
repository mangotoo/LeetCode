# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def linkedListToList(self, head):
        
        if head is not None:
            
            current_node = head
            values = list()
            
            while current_node:
                values.append(current_node.val)
                current_node = current_node.next
            
            return values
        else:
            return head
        
    def binarySearch(self, nums, low, high):
        
        if high<low:
            return None
        
        else:
            
            middle = (low + high)//2
            node = TreeNode(nums[middle])
            node.left = self.binarySearch(nums, low, middle -1)
            node.right = self.binarySearch(nums, middle + 1, high)
            
        return node
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        values = self.linkedListToList(head)
        
        if values:
            return self.binarySearch(values, 0, len(values) - 1)
        else:
            return None
        
        