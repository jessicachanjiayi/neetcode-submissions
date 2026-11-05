class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in HashMap:
                return [HashMap[diff],i]
            HashMap[n]=i
        return 
    
    # Check if the difference is in the HashMap, otherwise store the value in the list as key in the HashMap, and store its index as value, so if there's a difference that can match any key in the HashMap
            

            