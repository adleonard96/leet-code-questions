# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        if start is None or start.next is None:
            return head

        while start.next is not None:
            if start.val == start.next.val:
                start.next = start.next.next
            else: 
                start = start.next