class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 1  # This keeps track of our current multiplier (2^depth)
        
        for i in range(len(s)):
            if s[i] == '(':
                depth *= 2  # Going deeper doubles the potential score
            else:
                depth //= 2  # Stepping out halves the potential score
                
                # Check if this ')' forms an immediate "()" core
                if s[i - 1] == '(':
                    score += depth  # Add the doubled score of this core
                    
        return score