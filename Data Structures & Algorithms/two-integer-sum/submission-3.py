class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(nums):
            difference = target - number
            if(difference in seen):
                return [seen[difference], index]
            seen[number] = index