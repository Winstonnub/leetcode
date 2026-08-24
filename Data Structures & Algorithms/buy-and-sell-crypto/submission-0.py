class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current = prices[0]
        res = 0
        for i, n in enumerate(prices):
            if n <= current:
                current = n
            res = max(res, n - current)
        return res