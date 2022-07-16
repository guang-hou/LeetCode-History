from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = PriorityQueue()
        
        count = Counter(nums)
        print(count)
        
        for key in count:
            pq.put((-count[key], key))
        
        res = []
        
        for _ in range(k):
            val = pq.get()
            print(val)
            res.append(val[1])
            
        
        return res