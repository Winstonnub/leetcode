class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Flow
        # E.g. 5 + 3 (a + b)
        # 0101 + 0011
        # Sum bit = 0110 (5 ^ 3) 
        # Carry bit = 0001 (a & b) << 1
        # Then we just need to add the sum bit and carry bit together
        bitmask = (1 << 32) - 1 # 0111111... # to use bit mask, just use &
        while b != 0:
            a,b = (a ^ b) & bitmask, ((a & b) << 1) & bitmask
        if a > (1<<31):
            return ~(a ^ bitmask)
        return a 
         # ~(a ^ mask) is just fancy way of subtracting max number 2^32

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

    """4-bit version, M = 1111, a = 1110 (should decode to -2). Python ints have endless leading 0s, so a is really ...0000 1110.

a ^ M flips only the low 4: ...0000 0001
~ flips everything: ...1111 1110"""