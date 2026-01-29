from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr_pos = 1
        prev = None
        curr = head
        
        head_need_changed = False
        while curr:
            next = curr.next
            if left <= curr_pos and right >= curr_pos + 1:
                if not prev:
                    head_need_changed = True 
                else:
                    prev.next = curr
                
                curr.next = prev
            elif head_need_changed:
                head = prev
            
            prev = curr  
            curr = next    
                
            curr_pos += 1
            
        return head
        # if left == right:
        #     return head
        # prev = None
        # curr = head
        # left_node = None
        # left_prev = None
        # left_next = None
        # right_node = None
        # right_prev = None
        # right_next = None
        # prev = None
        # curr_pos = 1
        
        # while curr:
        #     if curr_pos == left:
        #         left_node = curr
        #         left_prev = prev
        #         left_next = curr.next
        #     if curr_pos == right:
        #         right_node = curr
        #         right_prev = prev 
        #         right_next = curr.next
        #     if left_node and right_node:
        #         if left_prev:
        #             left_prev.next = right_node
        #         right_node.next = left_next if left_next != right_node else left_node
        #         right_prev.next = left_node if right_prev != left_node else None
        #         left_node.next = right_next
        #         if left_prev is None:
        #             head = right_node
        #     curr_pos += 1
        #     prev = curr
        #     curr = curr.next
            
        # return head    
        # while curr:
        #     next = curr.next
        #     if left_pos == left:
        #         possibility = prev
        #     if (prev and left_pos == left) and (next and right_pos == right):
        #         prev.next = next.next
        #         next.next = curr
        #         possibility.next = next
        #         curr.next = prev
                
                
            
        #     prev = curr
        #     curr = next
        #     left_pos += 1
        #     right_pos += 1
    
Solution().reverseBetween(ListNode(1, 
                                   ListNode(2, 
                                            ListNode( 3, 
                                                     ListNode(4, 
                                                              ListNode(5))))), 2, 4)