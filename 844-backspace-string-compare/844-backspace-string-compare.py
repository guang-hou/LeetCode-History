class Solution:

    def get_string(self, s: str) -> str :
        bz = []
        for char in s :
            if char != '#' :
                bz.append(char) # 模拟入栈
            elif len(bz) > 0: # 栈非空才能弹栈
                bz.pop() # 模拟弹栈
        return str(bz)

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.get_string(s) == self.get_string(t)