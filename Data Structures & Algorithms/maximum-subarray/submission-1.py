class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm
        # Use of nums?
        currMax = 0
        res = nums[-1]
        # if it is negative, we drop it
        # [3,-7,9] # e.g. we just include 9. No need to include -7 after we go 'bankrupt'
        for i in range(0, len(nums)):
            currMax += nums[i]
            res = max(currMax, res)
            if currMax < 0:
                currMax = 0
        return res