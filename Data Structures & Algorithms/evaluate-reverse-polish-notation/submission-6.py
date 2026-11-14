class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in ["+","-","*","/"]:
                stack.append(int(ch))
            else:
                a = stack.pop()
                b = stack.pop()
                if ch == "+":
                    tmp =  b + a
                elif ch == "-":
                    tmp = b - a
                elif ch == "*":
                    tmp = b * a
                elif ch == "/":
                    tmp = int(b/a)
                stack.append(tmp)
            
        return stack[-1]
            


