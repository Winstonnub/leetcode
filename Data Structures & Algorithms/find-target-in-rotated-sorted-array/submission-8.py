class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,1,2]
        # mid is 5, if 3,4,5 is sorted, and if smallest in sorted  (3) bigger than 1, search right
        # else sort right
        # mid is 1, not sorted, if biggest in this chunk (2) bigger than 1, search right
        # else search left
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]: # left sorted
                if nums[l] <= target <= nums[m]: # search left (target is in the leftside)
                    r = m - 1
                else:
                    l = m + 1
            else: # right sorted
                if nums[m] < target <= nums[r]: # search right, target is in rightside 
                    l = m + 1
                else:
                    r = m - 1
        return -1
            
