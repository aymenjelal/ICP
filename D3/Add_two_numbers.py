class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        dig = ans
        carry =0
        while l1 or l2:
            digSum = ((l1.val if l1 else 0) + (l2.val if l2 else 0) +carry)%10
            carry = (int(l1.val if l1 else 0) + int(l2.val if l2 else 0) +carry)//10
            print(digSum)
            dig.next = ListNode(digSum)
            dig = dig.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        if(carry!=0):
            dig.next = ListNode(carry)
            dig = dig.next
            
            
        
        return ans.next