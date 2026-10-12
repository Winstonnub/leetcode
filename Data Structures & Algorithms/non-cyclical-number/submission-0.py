class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = []
        # Find each number
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            while n: # 19
                # Get 9
                digit = n % 10
                curr.append(digit ** 2)
                n //= 10 # 19 // 10 -> 1
            n = sum(curr)
            curr = []
        return True

