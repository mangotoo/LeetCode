class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not intervals:
            return []
        
        sorted_intervals = sorted(intervals, key = lambda interval: interval[0])
        
        merged_intervals = [sorted_intervals[0]]
        
        for interval in sorted_intervals[1:]:
            start = interval[0]
            end = interval[1]
            
            if merged_intervals[-1][1] >= start:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
            else:
                merged_intervals.append(interval)
                
        return merged_intervals