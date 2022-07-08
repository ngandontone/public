class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            current_Sum = numbers[l] + numbers[r]
            if current_Sum < target:
                l += 1
            elif current_Sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]