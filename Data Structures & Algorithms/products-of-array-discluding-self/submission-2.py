class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        array = [1]* len(nums)
        res = 1
        i = 0 

        while i < len(nums):
            j = 0
            while j < len(nums):
                if j == i:
                    j+=1
                    continue
                else:
                    res = res * nums[j]
                j+=1
            
            array[i] = res
            i+=1
            res = 1
        return array

        