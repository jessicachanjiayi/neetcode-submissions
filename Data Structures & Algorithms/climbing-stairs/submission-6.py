class Solution:
    def climbStairs(self, n: int) -> int:
        # Bottom-Up Dynamic Programming
        One,Two = 1,1

        for i in range(n-1):
            temp = One
            One = One + Two
            Two = temp
        return One  

        # Time Complexity O(n) since we iterate through the stairs once