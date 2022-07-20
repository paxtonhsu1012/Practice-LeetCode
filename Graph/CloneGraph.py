### https://leetcode.com/problems/clone-graph/
### Medium

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        q = deque([node])
        clone = {node.val: Node(node.val, [])}

        while q:
            curr = q.popleft()

            for n in curr.neighbors:
                if n.val not in clone:
                    clone[n.val] = Node(n.val, [])
                    q.append(n)

                clone[curr.val].neighbors.append(clone[n.val])

        return clone[node.val]
