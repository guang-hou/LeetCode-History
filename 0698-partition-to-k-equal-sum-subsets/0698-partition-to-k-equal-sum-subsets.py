class Solution:       
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        mask = 0
        memo = {}
        
        total = sum(nums) 
        target = total // k
        
        nums.sort(reverse=True)
        
        if total % k != 0:
            return False

        if nums[0] > target:
            return False
        
        bucketSum, filledBucketNum = 0, 0
        
        return self.backtrack(target, bucketSum, filledBucketNum, mask, memo, k, nums)
        
    def backtrack(self, target, bucketSum, filledBucketNum, mask, memo, k, nums):  
        # 到达一个node时,pathTotal是从root到这个node之前所有node的和
        # count是所有之前node的subset的个数

        if filledBucketNum == k:
            return True

        if bucketSum > target:
            return False

        if mask in memo:
            return memo[mask]

        for i in range(len(nums)):
            num = nums[i]
            if (mask >> i) & 1 == 0:
                # if i > 0 and nums[i] == nums[i - 1] and ((mask >> (i - 1)) & 1) == 0:
                #     continue

                # path.append(num)
                mask = mask | (1 << i)
                
                bucketSum += num
                if bucketSum == target:
                    filledBucketNum += 1  
                    bucketSum = 0

                if self.backtrack(target, bucketSum, filledBucketNum, mask, memo, k, nums):
                    return True

                if bucketSum == 0:
                    filledBucketNum -= 1
                    bucketSum = target
                    
                bucketSum -= num
                
                mask = mask ^ (1 << i)

                # path.pop()

        memo[mask] = False
    

        