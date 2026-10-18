class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        len1, len2 = len(s1), len(s2)
        dp = [[False] * (len2 + 1) for _ in range(len1 + 1)]
        dp[0][0] = True
        # dp[i][0] = dp[i-1][0] if last char match
        if len1 + len2 != len(s3):
            return False
        for i in range(1, len1 + 1):
            if s1[i - 1] == s3[i-1]:
                dp[i][0] = dp[i-1][0]
        for j in range(1, len2 + 1):
            if s2[j - 1] == s3[j-1]:
                dp[0][j] = dp[0][j-1]


        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if s1[i - 1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                if s2[j - 1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[len1][len2]
                