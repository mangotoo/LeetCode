from collections import deque

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        sub_list_sum = {0:1}
        count = 0
        current_sum = 0
        
        for num in nums:
            current_sum += num
            count += sub_list_sum.get(current_sum - k, 0)
            sub_list_sum[current_sum] =  sub_list_sum.get(current_sum, 0) + 1
            
        return count