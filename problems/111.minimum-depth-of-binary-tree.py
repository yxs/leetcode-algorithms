import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# dfs
class Solution:
    # 本题的定义，root节点的深度为1
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_depth = 10 ** 9

        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1

# bfs
class Solution2:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))

        return 0

