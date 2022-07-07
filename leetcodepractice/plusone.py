class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        significant_digits = len(digits)
        count = 1
        
        for i in range(len(digits)):
            count += digits[i] * (10 ** (significant_digits - 1 - i))
        
        result = [int(digit) for digit in str(count)]
        
        return result 