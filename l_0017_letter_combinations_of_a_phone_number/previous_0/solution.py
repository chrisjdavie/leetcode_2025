from typing import List

digits_to_letters: dict[str, str] = {
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

        combs: list[str] = [""]
        for d in digits:
            new_combs: list[str] = []
            for c in combs:
                new_combs.extend([c + l for l in digits_to_letters[d]])
            combs = new_combs
        return combs
