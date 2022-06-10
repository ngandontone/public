class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i,j]
        hashmap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            
            if difference in hashmap:
                return [hashmap[difference],i]
            hashmap[nums[i]] = i