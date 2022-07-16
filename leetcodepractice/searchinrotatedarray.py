class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        first = nums[0]
        while l <= r:
            midpoint = (l + r) // 2
            if nums[midpoint] == target:
                return midpoint
            
            i_am_big = nums[midpoint] >= first
            target_is_big = target >= first
            
            if i_am_big == target_is_big:
                if nums[midpoint] < target:
                    l = midpoint + 1
                else:
                    r = midpoint - 1
            else:
                if i_am_big:
                    l = midpoint + 1
                else:
                    r = midpoint - 1
        return -1 