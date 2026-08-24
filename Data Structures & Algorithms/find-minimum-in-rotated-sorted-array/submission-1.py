class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Example [3,4,5,1,2]
        # middle is 5, since 3 to 5 is sorted, we store 3 and look into right
        # middle is 1, since 3 to 1 is not sorted, we store 1 and look into left
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            
            m = (l+r) // 2
            if nums[m] >= nums[l]:
                res = min(res, nums[l])
                l = m + 1
            else:
                res = min(res, nums[m])
                r = m - 1
        return res
