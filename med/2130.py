# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        locator = head.next
        prev = head

        while locator != slow:
            prev = prev.next
            locator = locator.next
        end_of_first = prev
        curr = slow

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        end_of_first.next = prev
        
        ans = 0
        while head and mid:
            ans = max(head.val + mid.val, ans)
            head = head.next
            mid = mid.next

        return ans
    

Solution().pairSum(ListNode(5, ListNode(4, ListNode(2, ListNode(1)))))