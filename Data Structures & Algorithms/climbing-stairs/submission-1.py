class Solution:
    def climbStairs(self, n: int) -> int:
        # To reach step i, you either go 1 step from (n-1) step, or go 2 steps from (n-2) step, so ways to arrive at n step = ways to arrive at (n-1) step + ways to arrive at (n-2) step. Which is Ways(n)= Ways(n-1)+Ways(n-2), essentially a Fibonacci sequence: F(n)=F(n-1)+F(n-1)
        # Steps：1，2，3，5，8....
        # Fibonacci: 1,1,2,3,5...
        import math 
        sqrt5 = math.sqrt(5)
        PositiveSolution = (1+sqrt5)/2
        NegativeSolution = (1-sqrt5)/2
        n += 1 # The sequence of steps is a Fibonacci sequence starting at the second factor
        return round((PositiveSolution**n - NegativeSolution**n)/sqrt5)
        # Binet Formula
