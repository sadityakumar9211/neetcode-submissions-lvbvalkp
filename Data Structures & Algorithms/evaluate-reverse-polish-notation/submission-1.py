class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if ch == '+':
                    stack.append(str(int(a) + int(b)))
                elif ch == '-':
                    stack.append(str(int(a) - int(b)))
                elif ch == '*':
                    stack.append(str(int(a) * int(b)))
                elif ch == '/':
                    stack.append(str(int(int(a) / int(b))))
            else:
                stack.append(ch)
        
        return int(stack.pop())