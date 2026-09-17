class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # relation:
        # max profit at i is max(dp[i-1], num[i] + dp[i-2])
        # Basically max profit is
        # 1. You don't rob at i, you get max profit from i-1
        # 2. You rob at i, you get max profit from i-2 (don't rob i-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[n-1]