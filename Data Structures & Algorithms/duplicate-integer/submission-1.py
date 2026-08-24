class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h = dict()
        for n in nums:
            if n in h:
                return True
            else:
                h[n] = 1
        return False