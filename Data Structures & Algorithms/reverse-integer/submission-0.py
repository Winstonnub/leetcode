class Solution:
    def reverse(self, x: int) -> int:
        bound = [-(2**31), 2 ** 31 -1]
        word = str(x)
        res = deque([])
        neg = False
        for c in word:
            if c == "-":
                neg = True
            else:
                res.appendleft(c)
        if neg:
            res.appendleft("-") 
        reversed_number = int("".join(res))
        return reversed_number if reversed_number in range(bound[0], bound[1]) else 0
            