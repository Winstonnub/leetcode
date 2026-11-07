class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # diff = target - nums[i]
        hashmap = dict() # Store the value and its index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
        return -1
