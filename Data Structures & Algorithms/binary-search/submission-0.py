class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary Search: we find the middle. CHeck if middle is target.
        # If not, we check if middle is larger or smaller.
        # If middle is larger than target, then search in the left side.
        # If middle is smaller than target, then search in the right side.
        l, r = 0, len(nums) - 1
        while l <= r:
            i = (r+l)// 2
            mid = nums[i]
            if target == mid:
                return i
            elif target < mid:
                r = i -1
            elif target > mid:
                l = i+1
        return -1
        