
# Leetcode 121

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prices_sorted = sorted(prices)
        
        profits = []
        
        for i in range(len(prices_sorted)):
            j = len(prices_sorted)-1
            
            while j >= i:
                for a in range(len(prices)):
                    if prices[a] == prices_sorted[i]:
                        for b in range(a+1, len(prices)):
                            if prices[b] == prices_sorted[j]:
                                profits.append(prices[b] - prices[a])
                j -= 1
          
        if profits:
            return max(profits)
        else:
            return 0
            
            
# OR

class SolutionTwo:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse=True):
            return 0
        
        else:
            profits = []
            for i in range(len(prices)):
                for j in range(i+1, len(prices)):
                    if prices[j] - prices[i] > 0:
                        profits.append(prices[j] - prices[i])
                        
        return max(profits)
				
