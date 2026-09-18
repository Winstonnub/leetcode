class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top down
        # 1. Setup
        memo = {0:0, 1:0}
        start_state = len(cost)
        def dp(i):
        # 1. Base case
            if i in memo:
                return memo[i]
            res = 1e6
        # 3. Try every decision
            for choice in [1, 2]: # decision is either cost[:-1] or -2
               
                next_state = i - choice

                candidate = cost[next_state] + dp(next_state)

                # 4. Combine
                res = min(res, candidate)
            memo[i] = res
            return res
        res = dp(start_state)
        return res if res < 1e5 else -1