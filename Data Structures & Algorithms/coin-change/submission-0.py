class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[a] minimum coins needed to get amount a 
        dp = [amount+1]*(amount+1) 
        # 0..amount, amount+1 means maximum value
        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])
                    # coin = 4, a=7, dp[7]= 1 + dp[7-4]
        return dp[amount] if dp[amount] != amount+1 else -1

        # O(amount * Numer of Coins)