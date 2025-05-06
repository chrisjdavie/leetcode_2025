PARENS_MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack: list[str] = []

        for paren in s:
            if paren not in PARENS_MAP:
                stack.append(paren)
            else:
                latest: str = stack.pop()
                if latest != PARENS_MAP[paren]:
                    return False

        return not stack
