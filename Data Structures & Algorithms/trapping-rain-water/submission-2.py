class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0 :
            return 0
        
        maxL = [0]*n
        maxR = [0]*n
        res =0

        maxL[0] = height[0]
        for i in range(1,n):
            maxL[i] = max(maxL[i-1],height[i])
        
        maxR[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            maxR[i] = max(maxR[i+1],height[i])

        for i in range(n):
            water = min(maxL[i],maxR[i])-height[i]
            if water <= 0:
                continue
            else:
                res+=water
        
        return res

                
            


                

