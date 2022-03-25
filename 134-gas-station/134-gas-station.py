class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        rest = [0] * n
        
        if sum(gas) < sum(cost): return -1
        
        for i in range(n):
            rest[i] = gas[i] - cost[i]
        
        start, cur_sum = 0, 0
        for j in range(n):
            cur_sum += rest[j]
            if cur_sum < 0:
                start = j + 1
                cur_sum = 0
        
        return start
        