# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

from collections import deque

class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.values = deque([])
        
        while iterator.hasNext():
            value = iterator.next()
            self.values.appendleft(value)
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.values[-1]
        

    def next(self):
        """
        :rtype: int
        """
        value = self.values.pop()
        
        return value
    
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.values) >0:
            return True
        
        else:
            return False
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].