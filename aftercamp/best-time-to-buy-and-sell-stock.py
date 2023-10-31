class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = 0
        for idx in range(len(prices) - 1, -1, -1):
            if stack and stack[-1] > prices[idx]:
                ans = max(ans, stack[-1] - prices[idx])
            else:
                stack.append(prices[idx])

        return ans
        