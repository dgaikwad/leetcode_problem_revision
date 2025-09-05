# Problem Statement: https://leetcode.com/problems/concatenation-of-array/submissions/1759200368/

# Solution: https://www.youtube.com/watch?v=68isPRHgcFQ

class Solution:
    def getConcatenation(self, nums):
        ans = nums
        for index in range(len(nums)):
            ans.append(nums[index])
        return ans


class Solution:
    def getConcatenation(self, nums):
       return nums + nums

class Solution:
    def getConcatenation(self, nums):
        ans = []
        for _ in range(2):
            for no in nums:
                ans.append(no)
        return ans

