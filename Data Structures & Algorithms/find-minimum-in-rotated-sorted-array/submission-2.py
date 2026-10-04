class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1 #设定2 Pointers
        while l < r: #只要符合条件就一直检查
            mid = l+(r-l)//2
            if nums[mid] < nums[r]: #检查右边，最小值是否在右边
                r = mid # 最小值不在右边，只检查左边
            else:
                l = mid +1
        return nums[l]
