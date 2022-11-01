class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []
        
        self.backtrack(n, path, ans, 1, 0, 0)
        
        return ans
        
    def backtrack(self, n, path, ans, position, leftCount, rightCount):
        #print(path)
        if leftCount < rightCount:
            return
        
        if leftCount > n or rightCount > n:
            return
        
        if position == 2 * n + 1 and leftCount == rightCount:
            ans.append("".join(path))
            return
        
        path.append("(")
        self.backtrack(n, path, ans, position + 1, leftCount + 1, rightCount)
        path.pop()

        path.append(")")
        self.backtrack(n, path, ans, position + 1, leftCount, rightCount + 1)          
        path.pop()