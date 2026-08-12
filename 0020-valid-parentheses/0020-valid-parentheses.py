class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack=[]
        for ch in s:
            if ch in pairs:
                if not stack or pairs[ch] != stack.pop():
                    return False
            else:
                stack.append(ch)
        return not stack

        