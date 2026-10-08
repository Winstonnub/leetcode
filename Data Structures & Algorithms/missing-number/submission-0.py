class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        # Idea:
        # From Single Number, we know that a ^ a = 0, a ^ 0 = a
        # Intuition: XOR every number in range, then result is the missing number
        res = 0
        for num in nums:
            res ^= num
        for i in range(len(nums)+1):
            res ^= i
        return res