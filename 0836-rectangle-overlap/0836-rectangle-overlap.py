class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        
        # Check overlap on X-axis and Y-axis
        overlap_x = max(x1, x3) < min(x2, x4)
        overlap_y = max(y1, y3) < min(y2, y4)
        
        return overlap_x and overlap_y