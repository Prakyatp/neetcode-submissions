class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l = 0
        r = len(heights)-1

        while l < r:
            if heights[l]<heights[r]:
                volume = heights[l]*(r-l)
                res = max(res,volume)
                l+=1
            elif heights[l]>heights[r]:
                volume = heights[r]*(r-l)
                res = max(res,volume)
                r-=1
            else:
                volume = heights[l]*(r-l)
                res = max(res,volume)
                l+=1
        
        return res
