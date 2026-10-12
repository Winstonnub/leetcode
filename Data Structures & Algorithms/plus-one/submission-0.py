class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry
            if i == len(digits) -1: digits[i] += 1
            if digits[i] >= 10:
                digits[i] = digits[i] % 10
                carry = 1
            else:
                carry = 0
                break
        # If carry is still 1, we add it to the left
        if carry == 1:
            digits[0] = 1
            digits.append(0)
        return digits
