"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        
        def recurse(root, output):
            if not root.children:
                output.append(root.val)
            else:
                for child in root.children:
                    output = recurse(child,output)
                output.append(root.val)
            return output
        
        output = []
        if not root: return output
        
        output = recurse(root,output)
        return output