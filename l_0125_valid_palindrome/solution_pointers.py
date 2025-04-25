"""
Making it O(N) time and O(1) memory
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i_left: int = 0
        i_right: int = len(s) - 1
        is_palindrome: bool = True

        while i_left < i_right:
            if not s[i_left].isalnum():
                i_left += 1
            elif not s[i_right].isalnum():
                i_right -= 1
            elif s[i_left].lower() != s[i_right].lower():
                is_palindrome = False
                break
            else:
                i_left += 1
                i_right -= 1

        return is_palindrome
