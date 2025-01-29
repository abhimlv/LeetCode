from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i in strs:
            sorted_word = ''.join(sorted(i))
            anagrams[sorted_word].append(i)

        return list(anagrams.values())