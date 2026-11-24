class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Set up a HashMap dictionary to store the number we have already seen
        HashMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in HashMap:
                return [HashMap[diff],i]
            else:
                HashMap[n] = i
        return 

            

            