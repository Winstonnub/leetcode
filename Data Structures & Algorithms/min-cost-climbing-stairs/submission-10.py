class Solution:
     # To reach these two levels, it requires 0
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top down recursion with memoization
        memo = [-1] * len(cost)
        def dfs(i): # dfs returns the minimum total cost to move up 
            if i >= len(cost):
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2)) # min cost from step i+1 / i+2   
            return memo[i]
        return min(dfs(0), dfs(1))
        