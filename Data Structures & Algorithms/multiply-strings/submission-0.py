class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Idea is using the traditional multiplication method
        m = len(num1)
        n = len(num2)
        res = [0] * (m+n)
        output = []
        trailing = True
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                res[i+j+1] += int(num1[i]) * int(num2[j])
                if res[i+j+1] >= 10:
                    res[i+j] += res[i+j+1] // 10
                    res[i+j+1] %= 10
        for c in res:
            if c == 0 and trailing:
                continue
            else:
                trailing = False
                output.append(str(c))
        if not trailing:
            return "".join(output)
        return "0"
