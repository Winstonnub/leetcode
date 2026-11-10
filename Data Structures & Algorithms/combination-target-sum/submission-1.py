class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i, total):
            if total == target:
                res.append(curr.copy())
                return
            if i == len(nums) or total > target:
                return
            # Idea: the numbers can be reused, so i will not be height
            # Case 1: e.g. [2], we want to pick 2 (so pick itself)
            # Case 2: e.g. [2], we don't want to pick 2 anymore, CONSIDER 3 (not pick 3, but we can choose to pick or not pick 3)
            # Case 1: pick itself
            curr.append(nums[i])
            backtrack(i, total + nums[i])
            curr.pop()

            # Case 2: move to consider another number directly (so pick nothing)
            backtrack(i+1, total) # Then in this call, it can decide whether to pick 3
        backtrack(0,0)
        return res