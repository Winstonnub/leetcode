class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in h:
                return [h[difference], i]
            else:
                h[nums[i]] = i
        return []