class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        need = Counter(p)
        window = Counter(s[:len(p)])
        res = []
        if window == need:
            res.append(0)
        for i in range(len(p), len(s)):
            window[s[i]] += 1
            left_char = s[i - len(p)]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if window == need:
                res.append(i - len(p) + 1)
        return res