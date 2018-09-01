# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def max_depth(root, depth):         # if enter node -> depth +1 
            depth += 1
            depth_left = depth
            depth_right = depth
            if root.left:                   # if exist child -> recursion , if not ->return the maximun between left_depth and right_depth
                depth_left = max_depth(root.left,depth)
            if root.right:
                depth_right = max_depth(root.right, depth)
            return max(depth_left, depth_right)
        
        if not root:
            return 0
        depth =0
        depth = max_depth(root,depth) # recursion 
        return depth