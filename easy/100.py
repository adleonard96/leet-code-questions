# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(node):
            values = []
            if node is None:
                return [None]
            
            values += [node.val]
            values += traverse(node.left)
            values += traverse(node.right)

            return values

        return traverse(p) == traverse(q)
            
