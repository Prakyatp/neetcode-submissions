class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        x1 , y1 = 0, 0
        res = []
        
        for p in points:
            x2 , y2 = p[0], p[1]
            value = (math.sqrt((x1 - x2)**2 + (y1 - y2)**2))
            heapq.heappush(heap, [value,(x2,y2)])

        while k:
            distance, point = heapq.heappop(heap)
            res.append(point)
            k-=1
        
        return res
