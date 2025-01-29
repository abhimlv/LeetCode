class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
        
        """pow_var = 1
        if n == 0:
            return 1

        while n > 0:
            pow_var = pow_var * x
            n -= 1
        
        while n < 0:
            pow_var = pow_var / x
            n +=1
        
        return pow_var"""

        
