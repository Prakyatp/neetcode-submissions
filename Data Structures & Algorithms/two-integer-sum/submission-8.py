class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, a in enumerate(nums):
            res[a] = i 
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in res and res[diff]!=i:
                return [i,res[diff]]
        return []