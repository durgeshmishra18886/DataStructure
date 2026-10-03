class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the opening parenthesis
                stack.append(i)
            else:
                # Pop the last element (either an opening bracket or a boundary)
                stack.pop()
                
                if not stack:
                    # If stack is empty, the current closing parenthesis is invalid
                    # It becomes the new boundary for future valid substrings
                    stack.append(i)
                else:
                    # If stack is not empty, calculate the length of the valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len