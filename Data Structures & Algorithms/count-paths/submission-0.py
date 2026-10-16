class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Flow
        # dp = the number of possible ways the robot can take to reach dp[r][c]
        # Note that to reach dp[r][c] they can only be from the left (dp[r][c-1]) or top (dp[r-1][c])
        # Stage change: dp[r][c] = dp[r][c-1] + dp[r-1][c]
        
        # How do we avoid checking the bounds? We want to start in the inner square.
        # Notice the top and left column all have dp of 1, because they can only be reached in a straight line.
        # So let's initiate the entire dp board to be 1. Then we can overwrite the dp entries in the inner square.
        # m = no. rows, n = no. cols
        # State change: 
        dp = [[1] * n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r][c-1] + dp[r-1][c]
        return dp[m-1][n-1]

