class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 1. State:
        # dp[i][j] = min number of operations required to convert word1[:i] to word2[:j]
        # 2. Transitions
        # To get to dp[i][j], you come from some last state. 
        # If the last char are equal, no operation is needed (i.e. same as dp[i-1][j-1] expand the word and check next
        # If not equal (means we need to do operations! There are three choices: (Idea is if every last char match, every char match)
            # a. Insert: horse + s, ros (Now the both s matches, so problem reduced to dp[i][j-1] horse and ro)

            # b. Delete: horse - e, ros (Now hors and ros, so problem is now dp[i-1][j])

            # c. Replace: horse -> horss, ros (Now the both s mathces, so problem is reduced to dp[i-1][j-1] hors and ro)

            # We do not need to know what word we picked (dp does not store that). We just know we can pick the best word for that operation.
        # 3. Base case:
            # dp[0][0]: 0 # no op needed
            # dp[0][j]: j operations
            # dp[i][0]: i operations
        # 4. Code

        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
        for i in range(1, len1 + 1):
            dp[i][0] = i
        for j in range(1, len2 + 1):
            dp[0][j] = j
        
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                # if last char are same
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[len1][len2]