class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        lis = []
        res = []

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for key, value in freq.items():
            lis.append((-value, key))

        heapq.heapify(lis)

        while k:
            val, key = heapq.heappop(lis)
            res.append(key)
            k-=1

        return res

    

        



                 
            