class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False
        
        for char in s:
            if char == 'b':
                seen_b = True
            elif seen_b:  # char is 'a' after seeing a 'b'
                return False
                
        return True


        