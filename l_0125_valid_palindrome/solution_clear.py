class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_clean: str = "".join(s_i.lower() for s_i in s if s_i.isalnum())

        is_palindrome: bool = True
        for i in range(len(s_clean)//2):
            if s_clean[i] != s_clean[-i-1]:
                is_palindrome = False
                break

        return is_palindrome
