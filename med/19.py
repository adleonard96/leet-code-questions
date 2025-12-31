# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = ListNode(next=head)
        fast = ListNode(next=head)
        count = 0

        while fast.next:
            if count >= n:
                slow = slow.next
            count += 1
            fast = fast.next

        if slow.next == head:
            head = head.next
            return head

        slow.next = slow.next.next if slow.next else None
        return head