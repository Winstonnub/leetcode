class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Idea:
        # 4 ^ 4 = 0
        # 4 ^ 0 = 4
        # If 4 ^ 4 ^ 4 tho = 0 ^ 4 = 4, but we only have twice
        res = 0
        for x in nums:
            res = res ^ x
        return res