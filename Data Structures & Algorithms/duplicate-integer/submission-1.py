class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dict = {}
        # for num in nums:
        #     try:
        #         dict.update({num: dict[num] + 1}) 
        #     except:
        #         dict[num] = 1
        # for keys in dict:
        #     if dict[keys] > 1:
        #         return True
        # return False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
