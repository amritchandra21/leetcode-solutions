# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        forest = []

        def dfs(node, parent_delete):
            if not node:
                return None
            delete = False
            if node.val in to_delete:
                delete = True
            
            if parent_delete and not delete:
                forest.append(node)

            node.left = dfs(node.left, delete)
            node.right = dfs(node.right, delete)

            return None if delete else node
        dfs(root, True)
        return forest
            
            