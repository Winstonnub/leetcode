class Solution:
    def countBits(self, n: int) -> List[int]:
        # Idea
        # 7: 0111 (has 3) >> 011 (has 2) (So 7 equals to the no. bits of 7 >> 1 PLUS the last bit of 7)
        # 8: 1000 (has 1) >> 100 (has 1)
        # Recurrence Relation: dp[7] = dp[7 >> 1] + (7 & 1)
                            #  dp[i] = dp[i >> 1] + (i & 1)

        dp = [0] * (n+1)
        # dp[0] = 0 already
        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp