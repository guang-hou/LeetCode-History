from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = PriorityQueue()
        
        count = Counter(nums)
        
        res = []
        for key, val in count.most_common(k):
            res.append(key)
            
        return res