class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = {}
        stack = []
        
        # Step 1: Precompute matching parentheses positions
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
        
        # Step 2: Traverse with direction reversals
        res = []
        curr = 0
        direction = 1
        
        while curr < n:
            if s[curr] in '()':
                curr = pair[curr]
                direction = -direction
            else:
                res.append(s[curr])
            curr += direction
            
        return "".join(res)