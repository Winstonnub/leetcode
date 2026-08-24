class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = dict()
        tDict = dict()
        for x in s:
            if x not in sDict:
                sDict[x] = 1
            else:
                sDict[x] += 1
        for x in t:
            if x not in tDict:
                tDict[x] = 1
            else:
                tDict[x] += 1
        for y in sDict:
            if y in sDict and y in tDict:
                if sDict[y] != tDict[y]:
                    return False
            else:
                return False
        for y in tDict:
            if y in sDict and y in tDict:
                if sDict[y] != tDict[y]:
                    return False
            else:
                return False
        return True

        
        