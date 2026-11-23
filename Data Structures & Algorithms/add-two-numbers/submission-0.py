# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count1=0
        count2=0
        curr=l1
        while curr:
            curr=curr.next
            count1+=1
        curr=l2
        while curr:
            curr=curr.next
            count2+=1
        num1,num2=0,0
        
        curr=l1
        for i in range(count1):
            num1+=curr.val*(10**i)
            curr=curr.next
        curr=l2
        for j in range(count2):
            num2+=curr.val*(10**j)
            curr=curr.next
        final=str(num1+num2)
        dummy=ListNode(0,None)
        curr=dummy
        for k in final[::-1]:
            curr.next=ListNode(int(k),None)
            curr=curr.next
        return dummy.next
            
        


