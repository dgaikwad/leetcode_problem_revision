# Problem statement: https://leetcode.com/problems/longest-consecutive-sequence/description/
# Solution: https://www.youtube.com/watch?v=P6RZZMu_maU

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        data_set = set(nums)
        for no in nums:
            # Check wheather no-1 is avaibale or not to check the starting of the seq
            if (no - 1) not in data_set:

                lenght = 0
                while no + lenght in data_set:
                    lenght += 1
                longest = max(longest, lenght)
        return longest


