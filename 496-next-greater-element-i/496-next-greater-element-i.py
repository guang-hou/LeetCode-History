class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}   # item:next_greater_item
        
        stack = [nums2[0]]
        
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                item = stack.pop()
                next_greater[item] = nums2[i]
            stack.append(nums2[i])
        
        while stack:
            item = stack.pop()
            next_greater[item] = -1
        
        
        res = []
        
        for item in nums1:
            res.append(next_greater[item])
        
        return res