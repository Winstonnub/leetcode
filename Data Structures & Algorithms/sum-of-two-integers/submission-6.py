class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Flow
        # E.g. 5 + 3 (a + b)
        # 0101 + 0011
        # Sum bit = 0110 (5 ^ 3) 
        # Carry bit = 0001 (a & b) << 1
        # Then we just need to add the sum bit and carry bit together
        bitmask = 0xFFFFFFFF # to use bit mask, just use &
        while b != 0:
            a,b = (a ^ b) & bitmask, ((a & b) << 1) & bitmask
        return a if a <= 0x7FFFFFFF else ~(a ^ bitmask)
