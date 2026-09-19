class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Setup (l, r)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2 # Avoids overflow
            [1,3,5,7,9]
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1