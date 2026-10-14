class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        numset = set(nums)

        for n in numset:
            if (n-1) not in numset:
                falsec = 1
                while (n + falsec) in numset:
                    falsec+=1
                counter = max(falsec,counter)
        
        return counter
            

            
        