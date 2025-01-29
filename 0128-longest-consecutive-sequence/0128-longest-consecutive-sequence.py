class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Step 1: Create a set from nums
        max_length = 0
        
        for num in num_set:
            # Check if it's the start of a sequence
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                max_length = max(max_length, length)
        
        return max_length