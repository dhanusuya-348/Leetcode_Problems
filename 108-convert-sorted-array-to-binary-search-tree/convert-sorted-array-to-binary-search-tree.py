# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.buildBST(nums, 0, len(nums)-1)
    def buildBST(self, nums, left, right):
        if left>right:
            return None
        mid = left+(right-left)//2
        root = TreeNode(nums[mid])
        root.left = self.buildBST(nums, left, mid-1)
        root.right = self.buildBST(nums, mid+1, right)
        return root
         



        