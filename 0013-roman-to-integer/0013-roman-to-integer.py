class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0 # shows result
        prev = 0 # shows the previous character in the input from the back
        for char in s[::-1]: # iterates from last value of the input
            value = roman[char]
            if value < prev:
                result -= value
            else:
                result += value
            prev = value
        return result