"""
Code golfing, using Pythony things
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_clean: str = "".join(s_i.lower() for s_i in s if s_i.isalnum())
        return all(s_clean[i] == s_clean[-i-1] for i in range(len(s_clean)//2))
