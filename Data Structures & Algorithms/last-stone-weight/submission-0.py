
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            one_big = -heapq.heappop(heap)
            two_big = -heapq.heappop(heap)

            if one_big != two_big:
                new_stone = one_big - two_big
                heapq.heappush(heap, -new_stone)

        return -heap[0] if heap else 0
