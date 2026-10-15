class Solution:
    def numDecodings(self, s: str) -> int:
        # Valid if 1 <= number <= 26
        # dp[i] means the number of ways to decode up till index i
        def is_twodigit(x,y):
            if x == '0': return 0
            if 1 <= int(x + y) <= 26:
                return 1
            return 0
        n = len(s)
        if s[0] == '0':
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        # We only plus one if it can form a two-digit!
        for i in range(2, n+1):
            dp[i] = 0
            if s[i-1] != "0":
                dp[i] += dp[i-1]
            if is_twodigit(s[i-2], s[i-1]):
                dp[i] += dp[i-2]
        return dp[n]
        
        # Taking 1 digit is valid when this is not 0
        # Taking 2 digit is valid when the two digit is between 1 and 26