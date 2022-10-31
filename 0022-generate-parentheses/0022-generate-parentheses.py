class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []
        
        self.backtrack(n, path, 0, 0, ans)
        
        return ans
        
    def backtrack(self, n, path, leftCount, rightCount, ans):
        #print(path)
        if leftCount > n or rightCount > n:
            return
        
        if len(path) > 0 and path[0] == ")":
            return
        
        if len(path) == 2 * n:
            if self.isValid(path, n):
                #print("Yes")
                ans.append("".join(path))
            return
        
        
        for c in "(", ")":
            path.append(c)
            if c == "(":
                self.backtrack(n, path, leftCount + 1, rightCount, ans)
            else:
                self.backtrack(n, path, leftCount, rightCount + 1, ans)          
            path.pop()
                
        
    def isValid(self, path, n):
        stack = []
        
        for c in path:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] == ")":
                    return False
                else:
                    stack.pop()
        
        return len(stack) == 0