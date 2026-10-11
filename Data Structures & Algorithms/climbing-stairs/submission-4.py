class Solution:
    def climbStairs(self, n: int) -> int:
        # In simplied cases such as n=1/2/3/4 steps, we can easily figure out that there will be 1/2/3/5 ways to get there. The intution behind is The ways to get to n from i = The ways to get to n-1 from i + The ways to get to n-2 from i, so Ways[i]= Ways[i-1]+Ways[i-1], which is essentially a Fibonacci sequence.
        # So the first way will be doing math in Fibonacci:
        import math
        sqrt5 = math.sqrt(5)
        PositiveSolution = (1+sqrt5)/2
        NegativeSolution = (1-sqrt5)/2
        n = n+1
        return round((PositiveSolution**n-NegativeSolution**n)/sqrt5)