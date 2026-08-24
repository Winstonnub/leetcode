class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # HashMap
        hashmap = dict()
        for i, n in enumerate(nums): #(i = index 1,2..., n = value)
            hashmap[n] = i
        # if there is repeat, the last duplicate will be the indice.
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]
        return []