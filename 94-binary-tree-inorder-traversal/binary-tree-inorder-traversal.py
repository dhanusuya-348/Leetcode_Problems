# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        self.solve(root, result)
        return result
    def solve(self, root, result):
        if not root:
            return
        self.solve(root.left, result)
        result.append(root.val)
        self.solve(root.right, result)