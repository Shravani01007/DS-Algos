# Given a binary tree, flatten it to a linked list in-place.

# For example, given the following tree:

#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# The flattened tree should look like:

# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

    def printTree(self, root):
        while root:
            print(root.val)
            root = root.right


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(5)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(6)

a.left, a.right = b, c
b.left, b.right = d, e
c.right = f

soln = Solution()
soln.flatten(a)
soln.printTree(a)
