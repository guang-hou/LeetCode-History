from queue import PriorityQueue

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # record frequency : [keys]
        # ferquency will be between 0 and len(nums) + 1
        frq = [[] for _ in range(len(nums) + 1)]
        
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        res = []
        for cnt in range(len(nums), -1, -1):
            keys = frq[cnt]
            res.extend(frq[cnt])
            if len(res) >= k: return res[:k]

        #return res[:k]