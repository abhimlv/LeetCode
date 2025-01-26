class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        s = s.strip()

        for j in range(len(s)-1, -1, -1):
            if s[j] == ' ':
                break
            else:
                i += 1
    
        return i