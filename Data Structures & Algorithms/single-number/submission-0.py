class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Bit Manipulation
        index = 0
        for num in nums:
            index = index ^ num
        return index
