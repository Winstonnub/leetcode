class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Start at 0 or 1 :D
        # Set dp[i] to be the min cost of climbing stairs to level i 
        # min cost of climbing stairs to
        # level 1: 0
        # level 2: 0 or 10 -> 0
        # level 3: minimum of (cost to go level 1 and level 2) -> 10
        # Escape: minimum of level 2 and level 3 -> 0 + 15 and 10 + 20 -> pick 15
        n = len(cost) # We want to find the minCost of n+1 (to jump out!)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, n+1):
            dp[i] =  min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1]) # Find the total cheaper way to reach level i
        return dp[n]
        