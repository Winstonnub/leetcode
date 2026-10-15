class Solution:
    def countSubstrings(self, s: str) -> int:
        # Idea is, expand at each possible 'centre'
        # It is impossible to repeat since each palindrome only contributes at its own centres
        res = 0 # Number of Substrings
        # e.g. [aaa] , expand at i=0 we get a, expand at i=0 and i = 1 we get aa
        # expand at i=1 we get a, aaa, expand at i = 1 and i = 2 we get aa
        # expand at i = 2 we get a

        def expand(i):
            nonlocal res
            for l, r in ((i,i), (i, i+1)):
                while l in range(n) and r in range(n) and l <= r:
                    if s[l] == s[r]:
                        res += 1
                    else:
                        break
                    l -= 1
                    r += 1

        n = len(s)
        for i in range(n):
            expand(i)
        return res

        
