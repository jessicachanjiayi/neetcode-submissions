class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Instead of checking every possible stock price combination, we keep update the maximum Profit and minimum buy prices while going through every prices in the list, this decrease the time complexity from O(n^2) to O(n), as you don't need a nested loop but only go over constant elements in the price list
        maxP = 0
        minBuy = prices[0]
        for sell in prices:
            maxP = max(maxP, sell-minBuy)
            minBuy = min(minBuy, sell)
        return maxP

        
       
        
   
