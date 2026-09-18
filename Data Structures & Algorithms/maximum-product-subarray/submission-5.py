class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane's alg
        res = nums[0]
        currMin, currMax = 1, 1
        for n in nums:
            # we can think of dp[i-1] * n
            prevMin, prevMax = currMin, currMax
            currMin = min(prevMin * n, prevMax * n, n)
            currMax = max(prevMin * n, prevMax * n, n)
            res = max(res, currMax)
        return res
            