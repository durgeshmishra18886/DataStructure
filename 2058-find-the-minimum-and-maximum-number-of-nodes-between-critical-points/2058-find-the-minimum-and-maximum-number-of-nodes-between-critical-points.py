# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]

        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
    
        idx = 1
        prev = head
        curr = head.next

        while curr and curr.next:
            # Check if curr is a local maxima or minima
            is_max = curr.val > prev.val and curr.val > curr.next.val
            is_min = curr.val < prev.val and curr.val < curr.next.val

            if is_max or is_min:
                if first_cp == -1:
                    first_cp = idx
                else:
                    min_dist = min(min_dist, idx - prev_cp)
                prev_cp = idx

            prev = curr
            curr = curr.next
            idx += 1

    # If fewer than 2 critical points were found
        if first_cp == -1 or first_cp == prev_cp:
            return [-1, -1]

        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]
        