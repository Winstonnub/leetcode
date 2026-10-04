class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n: # while n is not zero! 
            res += n & 1 # Compare rightmost, is it 1?
            n >>= 1 # shift right by 1 (update rightmost)
        return res