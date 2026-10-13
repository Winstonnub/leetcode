class Solution:
    def rob(self, nums: list[int]) -> int:
        # Idea: we rob from the left to the right!
        # dp[i] = so far up to ith house, what is the max amount of money we can rob?
        # Two choices: choose the max between
        # dp[i] = Max of dp[i-2] + nums[i] VS dp[i-1]
        # At each choice, either rob today, or don't rob and rob yesterday
        n = len(nums)
        dp = [0] * n
        if n == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]