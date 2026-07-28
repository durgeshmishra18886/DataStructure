class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = sum2 = 0
        i = j = 0
        
        curr1 = l1
        while curr1:
            sum1 += curr1.val * (10**i)
            i += 1
            curr1 = curr1.next
            
    
        curr2 = l2
        while curr2:
            sum2 += curr2.val * (10**j)
            j += 1
            curr2 = curr2.next
            
        sum3 = sum1 + sum2 
        

        dummy = ListNode(0)
        curr = dummy
        
       
        for digit in str(sum3)[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
            
        return dummy.next