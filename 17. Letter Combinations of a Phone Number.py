class Solution(object):
    
    def combinationsHelper(self, digits, phone_map, choice, chosen):
        
        if len(digits) == 0:
            chosen.append(choice)
            
        else:
            for char in phone_map[digits[0]]:
                
                choice = choice + char
                
                self.combinationsHelper(digits[1:], phone_map, choice, chosen)
                
                choice = choice[:-1]
        
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        
        """
        
        digits = list(digits)
        
        chosen = list()
        
        if len(digits):
            phone_map = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
            
            self.combinationsHelper(digits, phone_map, '', chosen)
            
        return chosen       