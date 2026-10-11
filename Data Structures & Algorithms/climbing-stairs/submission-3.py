class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-Up Dynamic Programming, to reach step i, you either go from step (i-1) or go from step (i-2)，essentially a Fibonacci sequence，1/2/3/5/8...., this bottom-up DP fill the sequence from 1 on
        if n == 1:
            return 1 # 1 way to get to 1 from 0
        if n == 2:
            return 2 # 2 ways to get to 2 from 0
        dp = [0]* (n+1) # Create a DP array which stores the number of ways to reach step i
        dp[1], dp[2]= 1,2
        for i in range(3,n+1):
            dp[i]= dp[i-1]+dp[i-2]
        return dp[i]