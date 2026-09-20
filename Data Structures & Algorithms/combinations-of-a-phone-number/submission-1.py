class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8: 'tuv', 9: 'wxyz'}
        res = []
        cur = []
        if not digits:
            return []
        def backtracking(i): 
            if i >= len(digits):
                res.append("".join(cur.copy()))
                return
            
            for choice in hashmap[int(digits[i])]:
                cur.append(choice)
                backtracking(i+1)
                cur.pop()
        backtracking(0)
        return res
            