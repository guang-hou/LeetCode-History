class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_res = self.processBackspace(s)
        t_res = self.processBackspace(t)
        
        return s_res == t_res
                
    def processBackspace(self, str):
        
        processed = []
        space_count = 0
        
        for i in range(len(str) - 1, -1 , -1):
            if str[i] == '#':
                space_count +=1
            else:
                if space_count > 0:
                    space_count -= 1
                else:
                    processed.append(str[i])
        
        return "".join(processed)
                
                