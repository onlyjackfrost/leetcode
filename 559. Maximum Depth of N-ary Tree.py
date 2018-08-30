"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        if not root.children: return 1
        
        que = [root,"V"]
        depth = 0
        
        while len(que) > 0:
            node = que.pop(0)
            if node == "V":
                depth += 1
                if len(que) :
                    que.append("V")
                continue
            if node and node.children: 
                for child in node.children:
                    que.append(child)
        return depth
        