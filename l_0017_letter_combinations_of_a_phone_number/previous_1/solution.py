from typing import List

DIGITS_LETTERS_MAP: dict[int,str] = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",    
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        combs: List[str] = [""]
        for d in digits:
            new_combs: List[str] = []
            for c in combs:
                new_combs.extend(c + l for l in DIGITS_LETTERS_MAP[d])
            combs = new_combs

        return combs
