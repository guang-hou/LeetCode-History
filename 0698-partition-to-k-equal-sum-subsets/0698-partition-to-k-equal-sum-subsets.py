class Solution:       
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # path = []
        # used = [False] * len(nums)
        mask = 0
        memo = {}
        
        total = sum(nums) 
        subTotal = total // k
        
        nums.sort(reverse=True)
        
        if total % k != 0:
            return False

        if nums[0] > subTotal:
            return False
        
        def backtrack(startIndex, pathTotal, count, mask):  # 到达一个node时,pathTotal是从root到这个node之前所有node的和
                                          # count是所有之前node的subset的个数
            # print(path, pathTotal, count)
                
            if count == k:
                return True
            
            if pathTotal // subTotal != count:
                return False
            
            if mask in memo:
                return memo[mask]
            
            if pathTotal % subTotal == 0:
                startIndex = 0
            else:
                startIndex += 1
            
            for i in range(startIndex, len(nums)):
                num = nums[i]
                if (mask >> i) & 1 == 0:
                    if i > 0 and nums[i] == nums[i - 1] and ((mask >> (i - 1)) & 1) == 0:
                        continue
                    
                    # path.append(num)
                    mask = mask | (1 << i)
                    pathTotal += num
                    if pathTotal >= subTotal and pathTotal % subTotal == 0:
                        count += 1  
                        
                    if backtrack(startIndex, pathTotal, count, mask):
                        return True

                    if pathTotal >= subTotal and pathTotal % subTotal == 0:
                        count -= 1
                    pathTotal -= num
                    mask = mask ^ (1 << i)

                    # path.pop()
            
            memo[mask] = False
    
        return backtrack(0, 0, 0, 0)
        