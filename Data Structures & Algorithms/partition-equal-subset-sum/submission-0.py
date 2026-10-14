class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        target = total // 2 # Once we find out we can sum two subsets into HALF of nums, then the other half 
        #automatically satisfies
        if total % 2 == 1: # we cannot split odd total into half
            return False
        dp = [False] * (target + 1) # Is it possible to form this number (from coins we have used?)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):  # Set stop to be num, because base case is 0
                # The check is if i >= num (Since a number greater than i cannot sum up to i)
                dp[i] = dp[i] or dp[i - num] 
        return dp[target]
        