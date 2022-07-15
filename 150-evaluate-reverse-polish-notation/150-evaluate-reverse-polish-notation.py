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
                    res = num1 / num2
                    if res >= 0:
                        res = num1 // num2
                    else:
                        res = -(- num1 // num2)
                    num.append(res)
                print(num[-1])
        
        return num[0]
        