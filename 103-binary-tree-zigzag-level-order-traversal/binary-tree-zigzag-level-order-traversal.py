# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return []
        q = deque()
        q.append(root)
        count = 0
        while (q):
            levels = []
            for i in range(len(q)):
                qval = q.popleft()
                if (qval.left != None):
                    q.append(qval.left)
                if (qval.right != None):
                    q.append(qval.right)
                levels.append(qval.val)
            count += 1
            if count%2 == 0 :
                revlevels = levels[::-1]
                result.append(revlevels)
            else:
                result.append(levels)
        return result



        