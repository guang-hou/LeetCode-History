class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        cur_sum = 0
        min_sum = float('inf')
        
        for i in range(n):
            cur_sum += gas[i] - cost[i]
            min_sum = min(min_sum, cur_sum)
        
        if cur_sum < 0: return -1
        if min_sum >= 0: return 0
        
        for j in range(n - 1, 0, -1):
            min_sum += gas[j] - cost[j]
            if min_sum >= 0:
                return j
        
        return -1
        