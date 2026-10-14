class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        # Main idea:
        # dp[i]: the length of the longest increasing subsequence ending exactly at index i
        # We can guarantee dp[i] gives us the length of the subsequence ending AT i
        # If we are at num[i], we just loop through previous subsequence. If our number is larger, then we stick this num[i] onto the sequence, making the length dp[j] + 1. But we want to only keep the LARGEST. So use max.
        dp = [1] * n
        for i in range(0, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
