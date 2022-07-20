### https://leetcode.com/problems/binary-tree-level-order-traversal/
### Medium

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        q = deque()
        q.append(root)

        while q:
            levellen = len(q)

            tmp = []
            for _ in range(levellen):
                curr = q.popleft()
                tmp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            ans.append(tmp)

        return ans