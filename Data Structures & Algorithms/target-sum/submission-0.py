class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        # Idea:
        # For [1,2,1] and target = 2,
        # Say we are at the last index. Our number is 1.
        # To get to target = 2, it is only possible if we start at some number such that +1 or -1 equals 2.
        # So, ways to reach target 2 at 3rd number is the no. way to reach target 1 or -1 at 2nd number.
        # Transition
        # dp[i][j] = dp[currrent num index][target]
        # dp[i][j] = dp[current num index - 1][target - num[current]] + dp[current num index - 1][target + num[current]]
        # dp[i][j + total] = dp[i-1][j-num[i-1] + total] + dp[i-1][j+num[i-1] + total]  (note num[i-1] is curr num)
        # We need to shift every target amount by total so that target of -1 doesn't go wrong with indexing.
        
        # Rows are each number, col are each reachable target [-total, total]
        # Base case: with 0 numbers, target = 0 is the only 1 expression possible.
        # i is the ith number, j is the target sum
        total = sum(nums)
        if abs(target) > total: 
            return 0
        dp = [[0] * (2 * total + 1) for _ in range(len(nums) + 1)]
        dp[0][0 + total] = 1

        for i in range(1, len(nums) + 1):
            x = nums[i-1]
            for j in range(-total, total + 1):
                if -total <= j - x <= total:
                    dp[i][j + total] += dp[i-1][j-x + total] 
                if -total <= j + x <= total:
                    dp[i][j + total] += dp[i-1][j+x + total] 
        return dp[len(nums)][target + total] 
