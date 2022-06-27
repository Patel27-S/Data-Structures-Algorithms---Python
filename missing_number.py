# Leetcode 268

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        vals = [0]*(len(nums)+1)
        
        for x in nums:
            vals[x] += 1
        
        for i in range(len(vals)):
            if vals[i] == 0:
                return i
        
