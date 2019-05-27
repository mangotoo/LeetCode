class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        # [[1, 3],[5, 10], [6, 8]]
        
        if not intervals:
            return 0
        
        intervals_sorted = sorted(intervals, key = lambda interval : interval[0])
        
        priority_queue = list()
        heapq.heappush(priority_queue, intervals_sorted[0][1])
    
        for interval in intervals_sorted[1:]:
            
            if priority_queue[0] <= interval[0]:
                heapq.heappop(priority_queue)
                
            heapq.heappush(priority_queue, interval[1])
        return len(priority_queue)