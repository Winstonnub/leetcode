class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Implement with two pointers and a hashset
        # Go through the string:
        # z: add z to the hashset, count ++
        # x: add x to the hashset, count ++
        # y: add y to the hashset, count ++
        # z: z already in hashset, so we reset the set, move left pointer until no dupe
        # store if count is curr largest, then start over again
        
        l = 0
        res = 0
        hashset = set()
        for r in range(len(s)):
            while s[r] in hashset: # remove left until no dupe
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, r - l + 1)
        return res


