from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return []
        q = deque()
        q.append(root)
        while (q):
            levels = []
            for i in range(len(q)):
                qval = q.popleft()
                if (qval.left != None):
                    q.append(qval.left)
                if (qval.right != None):
                    q.append(qval.right)
                levels.append(qval.val)
            result.append(levels)
        return result



        