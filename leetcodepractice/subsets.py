class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        power_set = []
        
        subset = []
        def dfs(i):
            if i>= len(nums):
                power_set.append(subset.copy())
                return
            #decision includes nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            
            #decision does NOT include nums[i]
            subset.pop()
            dfs(i+1)
            
            
        dfs(0)
        return power_set