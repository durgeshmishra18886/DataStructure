class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_right = 0
        
        for ch in s:
            if ch == '(':
                # If we need an odd number of ')', the previous '(' only got one ')'
                if needed_right % 2 != 0:
                    insertions += 1    # Insert a ')' to complete the pair
                    needed_right -= 1  # Completed
                
                needed_right += 2      # Each '(' expects two ')'
            else:
                needed_right -= 1
                # Extra ')' found without a matching '('
                if needed_right < 0:
                    insertions += 1    # Insert an opening '('
                    needed_right += 2  # The inserted '(' expects 2, minus 1 current = 1
                    
        return insertions + needed_right