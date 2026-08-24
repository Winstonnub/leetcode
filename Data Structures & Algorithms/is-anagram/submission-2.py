class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1 = dict()
        h2 = dict()
        for x in s:
            if x not in h1:
                h1[x] = 1
            else:
                h1[x] += 1
        for x in t:
            if x not in h2:
                h2[x] = 1
            else:
                h2[x] += 1
        for k in h1:
            if k in h1 and k in h2:
                if h1[k] != h2[k]:
                    return False
            else:
                return False
        
        for k in h2:
            if k in h1 and k in h2:
                if h1[k] != h2[k]:
                    return False
            else:
                return False
        return True
            
