# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr=head
        listlen=0
        while curr:
            listlen+=1
            curr=curr.next
        curr=head
        if listlen<2:
            return None
        for i in range(math.ceil(listlen/2)-1):
            curr=curr.next
        nxt=curr.next
        curr.next=None
        curr=nxt
        prev=None
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        head2=prev
        head1=head
        for i in range(int(listlen/2)):
            nxt1=head1.next
            head1.next=head2
            head1=nxt1
            nxt2=head2.next
            if head1:
                head2.next=head1
                head2=nxt2



