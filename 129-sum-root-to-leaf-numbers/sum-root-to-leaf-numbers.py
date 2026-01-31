# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        def Sum(root, value):
            nonlocal res
            if not root:
                return None
            n = (10 * value) + root.val
            if not root.right and not root.left:
                res += n
                return None
            Sum(root.left, n)
            Sum(root.right, n)


        Sum(root, 0)
        return res