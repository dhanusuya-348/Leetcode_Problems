# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.validate(root, float('-inf'), float('inf'))
    def validate(self, node, lower, upper):
        if not node:
            return True
        if(node.val<=lower or node.val>=upper):
            return False
        return self.validate(node.left, lower, node.val) and self.validate(node.right, node.val, upper)
