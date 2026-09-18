class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Like sliding window 
        # Kadane's Algorithm: if running sum becomes negative, we reset and start it from next element.
        # Store: best subarray sum in this window, and global
        currSum = 0
        res = nums[0]
        for n in nums:
            currSum += n
            res = max(currSum, res)
            if currSum < 0:
                currSum = 0
        return res
