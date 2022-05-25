class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return True
            hashmap[nums[i]] = 1
        return False 