class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        res = []
        for x in strs:
            k = "".join(sorted(x))
            if k not in d:
                d[k] = [x]
            else:
                d[k].append(x)
        for sublist in d:
            res.append(d[sublist])
        return res

        