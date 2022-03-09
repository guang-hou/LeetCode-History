class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path, res = [], []
        
        def backtrack(startIndex):
            if len(path) > 1:
                res.append(path[:])
            
            for i in range(startIndex, len(nums)):
                if startIndex > 0 and nums[i] < nums[startIndex - 1]:
                    continue
                if nums[i] in nums[startIndex : i]:
                    continue
                    
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
                
        
        backtrack(0)
        
        return res