class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = sorted(stones)
        while(len(stones) > 1):
            print(stones)
            max = stones.pop()
            second_max = stones.pop()
            if(max - second_max != 0):
                stones.append(abs(max-second_max))
                stones = sorted(stones)
        if(len(stones) == 0):
            return 0
        return stones[0]