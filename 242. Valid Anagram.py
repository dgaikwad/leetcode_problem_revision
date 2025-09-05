class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        data = [0] * 26
        for index in range(len(s)):
            data[ord(s[index]) - ord("a")] -= 1
            data[ord(t[index]) - ord("a")] += 1
        return data == [0] * 26
