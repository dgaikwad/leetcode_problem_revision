# Problem Statement: https://leetcode.com/problems/longest-common-prefix/description/
# Solution https://www.youtube.com/watch?v=0sWShKIJoo4&t=3s

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""
        for index in range(len(strs[0])):
            for s in strs:
                if index == len(s) or s[index] != strs[0][index]:
                    return res
            res += strs[0][index]
        return res


"""
Explanation :

The Python code provided finds the **longest common prefix** among a list of strings. It works by iterating through the characters of the first string and, for each character, checking if it is also present at the same position in all the other strings.

***

### How the Code Works

The code's logic can be broken down into these steps:

1.  **Initialization**: The variable `res` is initialized as an empty string (`""`). This variable will store the longest common prefix as it is being built.

2.  **Outer Loop (Character Iteration)**: The code uses a `for` loop to iterate through the indices of the first string in the list (`strs[0]`). The `index` variable represents the position of the character being checked (e.g., `0` for the first character, `1` for the second, and so on).

3.  **Inner Loop (String Comparison)**: For each character from the first string, an inner `for` loop iterates through every string (`s`) in the input list `strs`. This is where the core comparison happens.

4.  **Prefix Check**: Inside the inner loop, two conditions are checked:
    * `index == len(s)`: This checks if the current string `s` is shorter than the first string. If it is, there can't be a common prefix extending beyond the length of `s`, so the loop is terminated.
    * `s[index] != strs[0][index]`: This checks if the character at the current `index` in the string `s` is different from the character at the same `index` in the first string (`strs[0]`).

5.  **Termination and Return**: If either of the two conditions in step 4 is true, it means the common prefix has ended. The code immediately returns the value currently stored in `res`, which holds the longest common prefix found so far.

6.  **Building the Prefix**: If the inner loop completes without returning, it means the character at the current `index` from the first string is common to all other strings. In this case, that character is appended to the `res` string (`res += strs[0][index]`).

7.  **Final Return**: After the outer loop has finished iterating through all the characters of the first string, the `res` string is returned. This happens if the first string itself is the longest common prefix (e.g., `["flower", "flow", "f"]`).

"""

