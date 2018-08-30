# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaf_root1 = []
        leaf_root2 = []
        
        def travel_root(root , leaf_root):
            if not root :
                return leaf_root
            elif not root.left and not root.right :
                leaf_root.append(root.val)
            else :
                travel_root(root.left , leaf_root)
                travel_root(root.right, leaf_root)
            return leaf_root
        
        leaf_root1 = travel_root(root1, leaf_root1)
        leaf_root2 = travel_root(root2, leaf_root2)
            
        return leaf_root1 == leaf_root2 