class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Reason through it!
        # State dp[i][j] stores the longest common subsequence of text1[:i] and text2[:j]
        # Transitions
        # What does dp[i][j] depend on? The longest common subsequence.
        # How can we reach dp[i][j]? From i-1, j-1, or both.
        # Two cases:
            # 1. abcde and ace: since both end with e, 
            # we can add 1 from the dp of abcd and ac (i.e. dp[i-1][j-1])
            # 2. abcd and ac: longest subsequence here is what? It is remove last character from each, and take max
            # abc and ac -> 2; abcd and a -> 1; so we know the current longest subseqeunce is 2 
            # max(dp[i-1][j], dp[i][j+1])
        # One note: i = 1 means first character. i = 0 is empty string ""
        len1, len2 = len(text1), len(text2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1] # if it is "a" == "a", then state dp "" was 0. So "a" and "a" is 1.
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # either abcd and ace VS abcde and ac (remove last)
        return dp[i][j]