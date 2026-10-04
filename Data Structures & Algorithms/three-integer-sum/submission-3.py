class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] #Create a dict to store results
        nums.sort() #Two Pointers need sorted numbers

        # Fix one number first, if this number>0, look at the other one, if this number equal to the last number, skip this one, it's unnecessary to check again. 
        for i,a in enumerate(nums):
            if a > 0: # 3 Sums will always be positive
                break
            if i > 0 and nums[i]==nums[i-1]: # meaningless to check the same number
                continue
            # Two Pointers, to check the other 2 numbers
            l, r = i+1, len(nums)-1
            while l < r:
                threeSums = a + nums[l]+nums[r]
                if threeSums > 0:
                    r -= 1  # Find a smaller number
                elif threeSums < 0:
                    l += 1  # Find a larger number
                else:
                    res.append([a,nums[l],nums[r]]) # Return the Dict
                    # Then we need to i+2,i+3....
                    l = l+1
                    r = r-1
                    while l < r and nums[l]==nums[l-1]:
                        l = l+1 # If the left pointer equals to the last one we already checked, we move on instead of keep doing
        return res

        