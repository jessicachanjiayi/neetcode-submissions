class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, n, n+1, n+2....]
        rob1, rob2 = 0,0
        for n in nums:
            n = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = n
        return rob2