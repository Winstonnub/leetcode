class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Best example
        # dp[i] = whether s[:i] can be built up by words in dictionary
        # "leetcodes", wordDict = ["leet", "codes"]
        # dp[0] = True # because "" can be built trivially
        # dp[1] = False ("l") no words can build that
        # dp[2] = False ("le")
        # dp[3] = False ("lee")
        # dp[4] = True ("leet"), i = 4, s[:4] in wordDict
        # dp[5]
        #...
        # dp[9] = True ("leetcodes")
        # We try leet, does not match s[9-4:9] # s[i - len(word):i] where word is from wordDict
        # We try codes, match s[9-5:9], so we update dp[9] = True and dp[9-5] # We also need dp[4] be true
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True # True since empty string can be built from nothing
        for i in range(1, n+1):
            # current word is s[:i]
            for word in wordDict:
                if len(word) <= i:
                    if s[i-len(word):i] == word:
                        dp[i] = dp[i] or dp[i-len(word)]
        return dp[n] 