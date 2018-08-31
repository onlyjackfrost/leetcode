# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        def switch_val(a,b):    #switch value
            tmp = a
            a = b
            b = tmp
            return a,b
        # VLR
        output = [root]
        if not root:
            return None
        #V if need to trim
        
        #L
        root.left = self.trimBST(root.left, L, R)
        #R
        root.right = self.trimBST(root.right, L, R)
        
        if root.val not in range(L, R+1):
            # 3 condition: 2 child, 1 child, no child
            if root.left and root.right: #2 children
                root.val, root.right.val = switch_val(root.val, root.right.val)
                root.right = self.trimBST(root.right, L, R)
                return root.right
            if root.right: # 1 child
                return root.right
            if root.left: # 1 child
                return root.left
            if not root.left and not root.right:
                root.val = None
                return None
         
           
        return root