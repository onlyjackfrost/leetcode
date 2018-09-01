"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def traversal(root, output):  
            #VLR,  v : append root.val into output
            output.append(root.val)
            if root.children:
                for child in root.children:  #from  L to R
                    child = traversal(child, output)
            return output
        
        output =[]
        if not root:
            return output
        output = traversal(root, output)
        return output