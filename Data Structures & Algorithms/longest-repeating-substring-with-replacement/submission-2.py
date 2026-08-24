class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use two pointers, hashmap, sliding window
        # Idea: use a sliding window.
        # The sliding window is valid if length of window - max freq element <= k
        # if not, then we move l, decrement count by 1 for that char, then check again
        l = 0 
        res = 0
        count = defaultdict(int) #default value is 0
        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


            
