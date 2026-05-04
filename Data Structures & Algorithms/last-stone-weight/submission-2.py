from heapq import heappop, heappush, heapify

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = []
        heapify(stones_heap)
        for stone in stones:
            heappush(stones_heap,-1*(stone))
        while len(stones_heap) > 1:
            max = heappop(stones_heap)
            second_max = heappop(stones_heap)
            diff = abs((-1*max) - (-1*second_max))
            if(diff > 0):
                heappush(stones_heap,-1*diff)
            
        if(len(stones_heap) == 0):
            return 0 
        return -1*heappop(stones_heap)
