
roman_int_map: dict[str, int] = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:

        value: int = 0

        i = 0
        while i < len(s):
            if  i < len(s) - 1 and (cand := s[i] + s[i+1]) in roman_int_map:
                value += roman_int_map[cand]
                i += 2
            else:
                value += roman_int_map[s[i]]
                i += 1

        return value
