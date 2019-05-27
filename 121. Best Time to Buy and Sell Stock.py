class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        max_profit = 0
        min_price = max(prices)
        
        for index in range(len(prices)):
            
            current_price = prices[index]
        
            min_price = min(min_price, current_price)
            max_profit = max(max_profit, current_price - min_price)
    
                
        return max_profit