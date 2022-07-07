class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            
            
            if n == 1:
                return True
            
        return False
    
    
    def sumOfSquares(self, n: int) -> bool:
        sum = 0
        for digit in str(n):
            sum += int(digit) ** 2
        
        return sum