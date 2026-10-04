class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l < r:
            m = l + (r-l)//2
            if nums[m]<nums[r]:
                r = m #如果中间值比右边小，那最小值在左边，看左边的区域
            else:
                l = m+1
        return nums[l]