from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        current = root
        if len(nums) % 2 == 0:
            right_nodes = nums[mid:]
            left_nodes = nums[:mid]
        else:
            right_nodes = nums[mid + 1:]
            left_nodes = nums[:mid]
            
        right_nodes.reverse()
        left_nodes.reverse()
        for num in right_nodes:
            if num > current.val:
                current.right = TreeNode(num)
                current = current.right
            else:
                current.left = TreeNode(num)
                current = current.left

        current = root

        for num in left_nodes:
            current.left = TreeNode(num)
            current = current.left
    
        return root
    
    
sortedArrayToBST([-10,-3,0,5,9])