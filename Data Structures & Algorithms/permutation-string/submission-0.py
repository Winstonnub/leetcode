class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        windowsize = len(s1) # e.g 3 for abc
        arr1 = [0 for i in range(26)] # 26 characters
        arr2 = [0 for i in range(26)]

        # put s1 and sliding window into the arrays
        for i in range(windowsize):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1

        l, r = 0, windowsize #lecabee 
        for i in range(len(s1), len(s2)):
            if arr1 == arr2: return True
            else:
                arr2[ord(s2[l]) - ord('a')] -= 1
                arr2[ord(s2[r]) - ord('a')] += 1
                l += 1
                r += 1
        return arr1 == arr2

             




            

            