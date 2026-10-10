class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = set()
        reachable.add(0)
        for i, n in enumerate(nums):
            # e.g. [1,2,1,0,1]
            # Of course index 0 is reachable
            # if we are not at the end (equal len - 1) and this index is reachable
            # then for each index we can reach from this index, we set them to be reachable
            if i < len(nums) - 1 and i in reachable:
                for j in range(i+1, i+n+1):
                    reachable.add(j)
            elif i not in reachable:
                return False
        return True
