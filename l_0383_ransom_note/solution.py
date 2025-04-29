from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        note_count: Counter[str, int] = Counter(ransomNote)
        mag_count: Counter[str, int] = Counter(magazine)

        for letter, count in note_count.items():
            if mag_count[letter] < count:
                return False
        return True
