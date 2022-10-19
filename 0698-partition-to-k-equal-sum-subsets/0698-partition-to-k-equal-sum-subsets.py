class Solution:       
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # path = []
        used = [False] * len(nums)
        
        total = sum(nums) 
        subTotal = total // k
        
        nums.sort(reverse=True)
        
        if total % k != 0:
            return False

        if nums[0] > subTotal:
            return False
        
        @cache
        def backtrack(startIndex, pathTotal, count):  # 到达一个node时,pathTotal是从root到这个node之前所有node的和
                                          # count是所有之前node的subset的个数
            # print(path, pathTotal, count)
                
            if count == k:
                return True
            
            if pathTotal // subTotal != count:
                return False
            
            if pathTotal % subTotal == 0:
                startIndex = 0
            else:
                startIndex += 1
            
            for i in range(startIndex, len(nums)):
                num = nums[i]
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    
                    # path.append(num)
                    used[i] = True
                    pathTotal += num
                    if pathTotal >= subTotal and pathTotal % subTotal == 0:
                        count += 1  
                        
                    if backtrack(startIndex, pathTotal, count):
                        return True

                    if pathTotal >= subTotal and pathTotal % subTotal == 0:
                        count -= 1
                    pathTotal -= num
                    used[i] = False

                    # path.pop()
    
    
        return backtrack(0, 0, 0)
        