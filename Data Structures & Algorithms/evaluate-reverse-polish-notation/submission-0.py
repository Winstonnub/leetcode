class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-*/"
        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                b, a = stack.pop(), stack.pop()
                if s == "+":
                    stack.append(a+b)
                if s == "-":
                    stack.append(a-b)
                if s == "*":
                    stack.append(a*b)
                if s == "/":
                    stack.append(int(float(a)/b))
        return stack.pop()