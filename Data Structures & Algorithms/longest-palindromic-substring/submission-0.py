class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longestLeft, longestRight = 0, 0
        def expand(i):
            nonlocal longestLeft
            nonlocal longestRight
            longestLength = longestRight - longestLeft + 1
            for l, r in ((i, i), (i, i+1)):
                while l in range(n) and r in range(n) and s[l] == s[r]:
                    currLength = r - l + 1
                    if currLength > longestLength:
                        longestLeft, longestRight = l, r
                        longestLength = currLength
                    l -= 1
                    r += 1
        for i in range(n):
            expand(i)
        return s[longestLeft:longestRight + 1]