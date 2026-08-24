class Solution:
    def isPalindrome(self, s: str) -> bool:
        # We use two pointer algorithm: start left, right from either side

        newStr = ''
        # To clean the string to only alphanumeric
        for character in s:
            if character.isalnum():
                newStr += character.lower()

        left = 0 # First index of newStr
        right = len(newStr) - 1 # Last index of newStr
        while left <= right: # While left and right do not cross
            if newStr[left] != newStr[right]: # if the strings are not same
                return False
            left += 1
            right -= 1
        return True
            
