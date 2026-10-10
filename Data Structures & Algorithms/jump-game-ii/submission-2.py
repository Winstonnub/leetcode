class Solution:
    def jump(self, nums: List[int]) -> int:
        # What is the FARTHEST we can go?
        # Each time we update, it means we run out of jumps and we need to extend it
        farthest_indice = 0
        curr_farthest  = 0
        jump_count = 0
        if len(nums) == 1: return 0 # Base Case
        for i, n in enumerate(nums):
            # So, what is the farthest we can jump from indice 1? # that is indice 2. Let's say for indice 1, it is 1. then farthest is still 2. But if it is 4, then farthest is not 2, but 6. So we can jump.\
            if i <= farthest_indice:
                curr_farthest = max(curr_farthest, i + n)
            if i == farthest_indice: # we can break out of current maximum!
                farthest_indice = max(farthest_indice, curr_farthest)
                jump_count += 1
            if farthest_indice >= len(nums) - 1:
                return jump_count
        return jump_count