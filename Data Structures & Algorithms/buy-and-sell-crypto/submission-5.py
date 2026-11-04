class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1,len(prices)):
                sell = prices[j]
                Profit = sell - buy
                maxP = max(maxP,Profit)
        return maxP
        
       
        
   
