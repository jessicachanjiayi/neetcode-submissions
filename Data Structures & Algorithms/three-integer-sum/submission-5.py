class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 固定一个x,对其他的x进行Two Pointers，首先Two Pointers需要适用于sorted data, 要新建一个list来存储结果
        result = []
        nums.sort()
        # 对于这个固定的X，如果大于0了，那就没必要再看，如果它和上一个我们检查过的数值一样，那也没必要看了
        for i,a in enumerate(nums):
            if i > 0 and a > 0:
                break
            if i > 0 and nums[i]==nums[i-1]:
                continue
                # 接下来处理剩下的两个数值
            l,r = i+1, len(nums)-1
            while l < r:
                threeSums = a + nums[l]+nums[r]
                if threeSums > 0:
                    r = r-1
                elif threeSums < 0:
                    l = l+1
                else:
                    result.append([a,nums[l],nums[r]])
                    #以上是每一个组合的处理流程，现在要让流程动起来
                    l = l+1
                    r = r-1
                    while l<r and nums[l]==nums[l-1]:
                            l = l+1
        return result
