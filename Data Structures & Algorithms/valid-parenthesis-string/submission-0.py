class Solution:
    def checkValidString(self, s: str) -> bool:
        # Idea: use lo hi for *
        # balance: +1 for (, -1 for )
        # So idea is, if our 0 is in range of lo hi balance (lo <= 0 <= hi)
        # Then valid
        lo = 0
        hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            if hi < 0:
                return False
            lo = max(lo, 0) # e.g. **( cannot start with '))'!
        return True if lo <= 0 <= hi else False