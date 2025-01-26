class Solution:
    def mySqrt(self, x: int) -> int:
        pre = 0.0001
        guess = x/2
        while abs(guess * guess - x) > pre:
            guess = (guess + x/guess)/2
        
        return int(guess)