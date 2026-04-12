class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if ch == '+':
                    stack.append(int(a) + int(b))
                elif ch == '-':
                    stack.append(int(a) - int(b))
                elif ch == '*':
                    stack.append(int(a) * int(b))
                elif ch == '/':
                    stack.append(int(int(a) / int(b)))
            else:
                stack.append(int(ch))
        
        return int(stack.pop())