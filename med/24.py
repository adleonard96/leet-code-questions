# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        if head and head.next:
            head = head.next
        while current and current.next:
            following = current.next.next
            current.next.next = current 
            if prev:
                prev.next = current.next
            prev = current
            current.next = following
            current = current.next
