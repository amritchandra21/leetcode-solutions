# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([(root, 0)])
        maxInd = 0
        minInd = 0
        colMap = defaultdict(list)
        while q:
            node, col = q.popleft()
            maxInd = max(col, maxInd)
            minInd = min(col, minInd)
            colMap[col].append(node.val)

            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        
        res = []
        for c in range(minInd, maxInd + 1):
            res.append(colMap[c])
        return res
            