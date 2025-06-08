class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = None
        current = None

        if list1 != None and list2 != None:
            if list1.val < list2.val:             
                merged = ListNode(list1.val)
                current = merged
                list1 = list1.next
            else:
                merged = ListNode(list2.val)
                current = merged
                list2 = list2.next
        elif list1 != None:
            merged = ListNode(list1.val)
            current = merged
            list1 = list1.next
        elif list2 != None:
            merged = ListNode(list2.val)
            current = merged
            list2 = list2.next
            
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                new = ListNode(list1.val)
                current.next = new
                current = new
                list1 = list1.next
            else:
                new = ListNode(list2.val)
                current.next = new
                current = new
                list2 = list2.next
        
        while list1 != None:
            new = ListNode(list1.val)
            current.next = new
            current = new
            list1 = list1.next
             
        while list2 != None:
            new = ListNode(list2.val)
            current.next = new
            current = new
            list2 = list2.next
        
        return merged