class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start, cur_sum = 0, 0
        
        if sum(gas) < sum(cost): return -1
        
        for i in range(n):
            rest = gas[i] - cost[i]
            cur_sum += rest
            if cur_sum < 0:
                start = i + 1
                cur_sum = 0
        
        return start
        