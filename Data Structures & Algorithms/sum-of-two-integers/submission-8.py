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
        return a if a <= 0x7FFFFFFF else ~(a ^ bitmask) # ~(a ^ mask) is just fancy way of subtracting max number 2^32

        # More intuitive 
        '''
        def add32(a, b):
            mask = (1 << 32) - 1
            a, b = a & mask, b & mask
            while b:
                a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            return a if a < (1 << 31) else a - (1 << 32)

      1110  (14)
    - 10000 (16)
    = -2
    '''