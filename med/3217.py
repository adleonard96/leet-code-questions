# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        if head.val in nums:
            while head.val in nums:
                head = head.next 

        current = head

        while current.next:
            if current.next.val in nums:
                current.next = current.next.next
            else:
                current = current.next

        return head

        