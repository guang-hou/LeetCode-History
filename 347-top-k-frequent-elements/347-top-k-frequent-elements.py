class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # record frequency : [keys]
        # ferquency will be between 0 and len(nums) + 1
        count = {}
        frq = [[] for _ in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, cnt in count.items():
            frq[cnt].append(num)

        res = []
        for cnt in range(len(nums), -1, -1):
            keys = frq[cnt]
            res.extend(frq[cnt])
            if len(res) >= k: 
                return res[:k]