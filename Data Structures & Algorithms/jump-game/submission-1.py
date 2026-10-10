class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest_indice = 0
        for i, n in enumerate(nums):
            # 1. Can we step on this?
            if i <= farthest_indice: # e.g. farthest we can reach is 2,  we try to start from 2
                # valid
                farthest_indice = max(farthest_indice, i + n)
            else:
                return False
        return True
                