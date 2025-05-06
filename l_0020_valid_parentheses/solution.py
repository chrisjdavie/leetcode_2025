PARENS_MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
}

class Solution:
    def isValid(self, s: str) -> bool:

        stack: list[str] = []

        for paren in s:
            if paren in PARENS_MAP:
                if not stack:
                    return False
                if stack.pop() != PARENS_MAP[paren]:
                    return False
            else:
                stack.append(paren)

        return not stack
