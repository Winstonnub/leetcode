class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        countT = Counter(t) # distribution of characters in t
        window = defaultdict(int) # current window
        have = 0
        need = len(countT) # how many characters we need to match
        res = [-1, -1]
        resLen = float("infinity") # Store the best window
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in countT and window[s[r]] == countT[s[r]]: 
                have += 1
            while have == need:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = r-l+1
                window[s[l]] -= 1 # shrink by removing char from window
                if s[l] in countT and window[s[l]] < countT[s[l]]: # if this is 
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""
                

