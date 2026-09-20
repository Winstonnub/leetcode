class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def backtracking(i):
            if i >= len(s):
                res.append(cur.copy())
                return
            # Choose left or right!
            # Pick left:
            # for choice in choices: choose one, dfs, undo
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j): # e.g. i = 0, j = 0, is "aab"'s a a palindrome? j = 1, is aa palin? ...
                    cur.append(s[i:j+1]) # we say 'a' from 'aab' is a palindrome! Now we are left with ab
                    backtracking(j+1) # we are moving to only considering 'ab'
                    cur.pop()

        backtracking(0)
        return res

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True



