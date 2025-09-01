# Problem statement: https://leetcode.com/problems/find-the-duplicate-number/
#
# Solution Link: https://www.youtube.com/watch?v=_n5MR8IxR6c


"""Solution 1 : Check every data with remaining sub list
Time Complexity: O(n^2)
Space Complexity: 0
"""
"""class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]"""


"""Solution 2: Sort the data and check every data with neighbore
Time Complexity: O(nlogn)
Space Complexity: O(1)
"""

"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                return nums[index]
"""

"""
Solution 3: Use the set data to store each data visted and check if data already occurs or not, If already occurs means the current pointed data is the duplicate because there is only one data is duplicate in the given data set
Time Complexity: O(n)
Space Complexity: O(n)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        my_set = set()
        for no in nums:
            if no in my_set:
                return no
            else:
                my_set.add(no)
"""


"""
Solution 4:
The first loop is for finding the meeting point of the slow and fast pointers, while the second loop is for finding the entry point of the cycle, which is the duplicate number. This algorithm is known as Floyd's Tortoise and Hare algorithm, a clever way to detect a cycle in a linked list. In this problem, the array can be viewed as a linked list where each index points to the value at that index.

First Loop: Detecting a Cycle 🐢🐇
In the first loop, we use two pointers, slow and fast, that traverse the array at different speeds. The slow pointer moves one step at a time (slow = nums[slow]), while the fast pointer moves two steps at a time (fast = nums[nums[fast]]).

The existence of a duplicate number creates a cycle in the sequence of pointers. For example, if nums = [1, 3, 4, 2, 2], the sequence of pointers is 0→1→3→2→4→2→.... The cycle is 2→4→2→.... Because the fast pointer moves at twice the speed of the slow pointer, it is guaranteed to eventually catch up to the slow pointer if a cycle exists. The loop breaks when slow == fast, meaning the two pointers have met at some point within the cycle.

Second Loop: Finding the Start of the Cycle 🧐
The second loop starts a new pointer, slow2, from the beginning of the "list" (index 0), while the original slow pointer remains at the meeting point found in the first loop. Both pointers now move at the same pace, one step at a time (slow = nums[slow] and slow2 = nums[slow2]).

The mathematical proof behind this part of the algorithm shows that the distance from the start of the "list" to the cycle's entry point is the same as the distance from the meeting point to the cycle's entry point. Therefore, when slow and slow2 meet, they will be at the very beginning of the cycle, which corresponds to the duplicate number. The loop then returns this value.


Time Complexity: O(n)
Space Complexity: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

"""