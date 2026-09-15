class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Idea: we use hashmap
        # We know that target - n = diff
        # and if diff is in the hashmap, then we can return the index

        # 1. Setup
        # Define dictionary to store (number: index)
        # 2. We set up a loop to go through each number: (curr)
        # in each iteration we calculate the difference = target - curr
        # If difference is not in hashmap, we put hashmap[curr] = currindex
        # If difference in hashmap, then we return (hashmap[difference], currindex)
        hashmap = dict()
        for i, n in enumerate(nums): # index, number
            diff = target - n # 7 - 3 = 4
            if diff not in hashmap:# 4 is not in hashmap
                hashmap[n] = i # We put 3 in hashmap
            else:
                return [hashmap[diff], i]
        return []
        