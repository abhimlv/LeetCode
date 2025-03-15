class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        
        pref = strs[0]

        for s in strs[1:]:
            while not s.startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return ""
        
        return pref