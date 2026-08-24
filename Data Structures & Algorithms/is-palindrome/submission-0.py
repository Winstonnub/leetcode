class Solution:
    def isPalindrome(self, s: str) -> bool:
        # We use two pointer algorithm: start left, right from either side

        newStr = ''
        # To clean the string to only alphanumeric
        for character in s:
            if character.isalnum():
                newStr += character.lower()

        left = 0
        right = len(newStr) - 1
        while left <= right:
            if newStr[left] != newStr[right]:
                return False
            left += 1
            right -= 1
        return True
            
