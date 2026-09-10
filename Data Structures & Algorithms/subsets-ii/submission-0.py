class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        nums.sort()
        # base case:
        def backtrack(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            # Go left (Choose the number)
            cur.append(nums[i])
            backtrack(i+1)
            cur.pop()
            # Go right (don't choose the number)
            # Need skip dupe: [1,1,2,2] Don't choose 1, so we skip two 1s'
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        backtrack(0)
        return res




