class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        first_sum = {}
        second_sum = {}
        res = 0
        
        for numi in nums1:
            for numj in nums2:
                first_sum[numi + numj] = first_sum.get(numi + numj, 0) + 1
        
        
        for numi in nums3:
            for numj in nums4:
                target = -(numi + numj)
                if target in first_sum:
                    res += first_sum[target]
        
        return res