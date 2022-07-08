class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        current = 0
        
        for i in range(len(nums)):
            if current < 0:
                current = 0
            current += nums[i]
            max_sub = max(max_sub, current)
            
        return max_sub 