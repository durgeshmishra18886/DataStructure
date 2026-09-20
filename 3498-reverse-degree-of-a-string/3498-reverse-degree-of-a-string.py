class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for index, char in enumerate(s, start=1):
            rev_alphabet_pos = 26 - (ord(char) - ord('a'))
            total += index * rev_alphabet_pos
        return total

        