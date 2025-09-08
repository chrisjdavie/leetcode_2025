from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged: list[str] = []
        for letter1, letter2 in zip_longest(word1, word2):
            if letter1:
                merged.append(letter1)
            if letter2:
                merged.append(letter2)
        return "".join(merged)
