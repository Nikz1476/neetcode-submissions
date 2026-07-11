# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #O(n),O(h)
        if root is None:
            return None

        # Swap left and right children
        root.left, root.right = root.right, root.left

        # Invert left subtree
        self.invertTree(root.left)

        # Invert right subtree
        self.invertTree(root.right)

        return root

        #O(n),O(n)
        # if root is None:
        #     return None

        # queue = deque()

        # queue.append(root)

        # while queue:

        #     node = queue.popleft()

        #     node.left, node.right = node.right, node.left

        #     if node.left:
        #         queue.append(node.left)

        #     if node.right:
        #         queue.append(node.right)

        # return root