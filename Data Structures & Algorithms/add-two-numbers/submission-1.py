class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_num(node):
            num, place = 0, 1
            while node:
                num += node.val * place
                place *= 10
                node = node.next
            return num

        total = to_num(l1) + to_num(l2)

        dummy = ListNode()
        curr = dummy
        for digit in reversed(str(total)):
            curr.next = ListNode(int(digit))
            curr = curr.next
        return dummy.next