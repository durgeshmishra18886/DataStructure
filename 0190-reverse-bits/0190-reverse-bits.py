class Solution:
    def reverseBits(self, n: int) -> int:
        n = n & 0xFFFFFFFF  
    
        reversed_num = 0
        
        
        for _ in range(32):
            
            reversed_num = (reversed_num << 1) | (n & 1)
           
            n >>= 1  
            
        
        if reversed_num >= 0x80000000:
            reversed_num -= 0x100000000
            
        return reversed_num
        