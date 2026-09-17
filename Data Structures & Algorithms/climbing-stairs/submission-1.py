class Solution:
    def climbStairs(self, n: int) -> int:
        # Idea
        # To reach step i, you only come from
        # i-1: 1 step
        # i-2: 2 steps
        # E.g. to reach 2, you only come from 1 (+1) or 0 + 1 + 1 or 0 + 2
        # Total ways to reach step i is sum of ways to reach the previous 2
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2 # To reach 1, we have 1 way. To reach 2, 2 ways
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]