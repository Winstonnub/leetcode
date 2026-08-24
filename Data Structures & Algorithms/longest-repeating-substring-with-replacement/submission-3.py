class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Use two pointers, hashmap, sliding window
        # Idea: use a sliding window.
        # The sliding window is valid if length of window - max freq element <= k
        # if not, then we move l, decrement count by 1 for that char, then check again
        l = 0 
        res = 0
        count = defaultdict(int) #default value is 0
        for r in range(len(s)): #1. Move sliding window to right
            count[s[r]] += 1 # 2. Increment count in hashmap
            while (r - l + 1) - max(count.values()) > k: #3. While the sliding window is not valid (we increment l and remove from count)
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) #4. recalculate the max window
        return res


            
