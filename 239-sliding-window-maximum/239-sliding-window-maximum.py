class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        
        for i in range(k):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
        
        res.append(queue[0])
        
        for j in range(k, len(nums)):
            if nums[j - k] == queue[0]:
                queue.popleft()
            while queue and nums[j] > queue[-1]:
                queue.pop()
            queue.append(nums[j])
            res.append(queue[0])
        
        return res