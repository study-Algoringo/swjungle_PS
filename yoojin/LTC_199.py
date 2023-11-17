from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque([root])

        while queue:
            rightMost = None
            for _ in range(len(queue)):
                current = queue.popleft()
                if current:
                    rightMost = current
                    queue.append(current.left)
                    queue.append(current.right)
            if rightMost:
                result.append(rightMost.val)
        return result