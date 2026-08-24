class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Idea is if a number - 1 does not exist, 
        # then number is the start of a sequence
        # So we use hashset to verify all possble starts and keep track of length
        # Note hashset operations are O(1)
        hashset = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in hashset:
                length = 0
                k = 0
                while (num + k) in hashset:
                    k += 1
                longest = max(k, longest)
        return longest
