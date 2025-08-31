#Basically remove the duplicate character from the char and make output as asc order while building the result
#
#Leetcode problem: https://leetcode.com/problems/remove-duplicate-letters/description/
#Solution: https://www.youtube.com/watch?v=HjvMWNHZBNI
#program is below:


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # To store last occurneces of each char
        last_occurance = { item: index for index, item in enumerate(s)}
        # Data Container to create result
        stack = []
        seen = set()
        for index, char in enumerate(s):
            if char not in seen: # Checking data in set data type fast than list data type
                """
                "We need to remove data from the stack until it is empty. Alternatively, we can 
                remove data until the last item in the list is no longer greater than the current 
                character and if the last occurrence of a character is high, 
                as that character will be encountered again in the next loop iteration."
                """
                while stack and stack[-1] > char and last_occurance[stack[-1]] > index:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)
        return "".join(stack)
