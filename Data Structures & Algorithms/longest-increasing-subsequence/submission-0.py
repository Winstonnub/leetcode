class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        # each dp should store the LIS number and the current largest in the sequence NO
        
        # dp[i]: the length of the longest increasing subsequence ending exactly at index i
        dp = [1] * n
        for i in range(0, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
