class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = []
        
        for t in tokens:
            if t not in "+-*/":
                num.append(int(t))
            else:
                num2 = num.pop()
                num1 = num.pop()
                if t == '+':
                    num.append(num1 + num2)
                elif t == '-':
                    num.append(num1 - num2)
                elif t == '*':
                    num.append(num1 * num2)
                elif t == '/':
                    num.append(int(num1 / num2))
                print(num[-1])
        
        return num[0]
        