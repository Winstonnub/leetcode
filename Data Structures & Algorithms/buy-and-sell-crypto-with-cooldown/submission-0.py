class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Idea: for each day, we can either be in 3 states
        # HOLD: stock at hand in end of day (can go to SELL)
        # SELL: sold today (can go to REST)
        # REST: no stock and did not sel (cam go to HOLD)
        # dp[i][s] = the max profit if we are at s that day
        # DP matrix: n x 3
        n = len(prices)
        dp = [[float("-inf")] * 3 for _ in range(n)]
        # 0 is hold, 1 is sell and 2 is rest
        dp[0][0] = -prices[0]
        dp[0][1] = float("-inf")
        dp[0][2] = 0
        for i in range(1,n):
            # 0: HOLD means there is a STOCK at hand (from HOLD or REST)
                # We already have a stock bought -> from HOLD
                # We buy a stock today -> from REST
            # 1: SELL means the stock was just SOLD today (from HOLD)
                # We sell a stock -> from HOLD
            # 2: REST means there is NO STOCK at hand (from SELL or REST)
                # We have no stocks now -> from SOLD or REST 
            dp[i][0] = max(dp[i-1][2] - prices[i], dp[i-1][0])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][2] = max(dp[i-1][2], dp[i-1][1])
        return max(dp[n-1][i] for i in range(3))

            