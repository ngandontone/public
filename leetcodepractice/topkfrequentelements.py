class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        frequency = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        
        
        for num, count in num_count.items():
            frequency[count].append(num)
            
        result = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                result.append(num)
                if len(result) == k:
                    return result 