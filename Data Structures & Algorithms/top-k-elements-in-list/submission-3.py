class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        heap = []

        for num in nums:
            res[num] = res.get(num,0)+1
        
        for key , value in res.items():
            heapq.heappush(heap,(value,key))
            if len(heap) > k :
                heapq.heappop(heap)
            
        resu = []
        for i in range(k):
            resu.append(heapq.heappop(heap)[1])

        return resu   


            