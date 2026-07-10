class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i not in "+-*/":
                s.append(int(i))
            else:
                lastNum = s.pop()
                firstNum = s.pop()
                if i == "+":
                    s.append(firstNum + lastNum )
                if i == "-":
                    s.append(firstNum - lastNum )
                if i == "*":
                    s.append(firstNum * lastNum )
                if i == "/":
                    s.append(int(firstNum / lastNum) )
        return int(s[0])
        