class Solution:
    def reverseBits(self, n: int) -> int:
        # Algorithm
        # 1. pop last number of n, shift right by 1
        # 2. shift left by 1 for res, push that number into right
        
        res = 0
        for i in range(32):
            # 1. pop last number of n, shift right by 1
            pop = n & 1 
            n >>= 1
            # 2. shift left by 1 for res, push that number into right
            res <<= 1
            res |= pop
        return res