class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = prices[0]
        left_index = 0
        right = prices[0]
        right_index = 0
        for i in range(0,len(prices)):
            if(left > prices[i]):
                left = prices[i]
                left_index = i
            elif(left < prices[i] and left_index < i):
                right = prices[i]
                right_index = i
            if(right_index > left_index):
                max_profit = max(right - left,max_profit)
        return max_profit