# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #O(n^2),O(h) - height of tree
        # def height(root):
        #     if not root:
        #         return 0

        #     return 1 + max(height(root.left), height(root.right))

        # if not root:
        #     return 0

        # left_height = height(root.left)
        # right_height = height(root.right)

        # left_diameter = self.diameterOfBinaryTree(root.left)
        # right_diameter = self.diameterOfBinaryTree(root.right)

        # return max(left_height + right_height,
        #            left_diameter,
        #            right_diameter)



        #O(n),O(h)
        diameter = 0

        def height(node):
            nonlocal diameter

            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            diameter = max(diameter, left + right)

            return 1 + max(left, right)

        height(root)
        return diameter