class Solution:
    def climbStairs(self, n: int) -> int:
        # Dynamic Programming, optimized recursion, the ways to get to n from step i = ways from step (i+1) to n + ways from step (i+2) to n, unlike doing a recursion, we store the result the first time we compute it and reuse it later
        cache = [-1]*n # Create an array where every factor is -1, representing we haven't calculated yet
        def dfs(i): # Define a function for recursion form step i
            if i == n:
                return 1 # your current location equal to your target, one successful rounte need to be counted
            if i > n:
                return 0 # your current location is higher than target, no way to still get to target
            if cache[i] != -1:
                return cache[i] # We already calculated before, don't over computing
            cache[i]= dfs(i+1) + dfs(i+2)
            return cache[i]
        return dfs(0)
        

