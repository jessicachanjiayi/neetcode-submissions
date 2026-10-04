class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 第一步是找到断点（最小值），然后就可以把数据分成两段（递增数据）；定义新函数，将来会用二分法分别在左边和右边找Target
        l, r = 0, len(nums)-1

        # 先找到断点（最小值）
        while l < r:
            mid = l+(r-l)//2
            if nums[mid]<nums[r]: # 最小值在左边
                r = mid 
            else: # nums[mid]>nums[r] #最小值在右边
                l = mid + 1
        pivot = l # 存储断点
    
        # 定义Binary Search的函数
        def BinarySearch(left:int, right:int):
            while left <= right: 
                mid = (left+right)//2
                if nums[mid]==target:
                    return mid # 找到Target
                elif nums[mid]> target: # 中间数太大，目标在左边
                    right = mid -1 
                else: # nums[mid]<target,中间数太小，目标在右边
                    left = mid + 1
            return -1

        # Apply the function into 被断点分成的两段
        result = BinarySearch(0, pivot-1) # 先看左端如何
        if result != -1: 
            return result # 找到目标就给出Index，没有就看右端
        return BinarySearch(pivot, len(nums)-1) # 看右端

