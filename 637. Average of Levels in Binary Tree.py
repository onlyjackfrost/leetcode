class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        #LRV  ,     V : calculate average value and clear node in the same level
        output = []
        child = [root, "X"]
        
        while len(child) != 1 :  #if have node in child
            x = child.index("X")
            for node in child[:x]: #append every child of node into child
                #L
                if node.left:
                    child.append(node.left)
                #R
                if node.right:
                    child.append(node.right)
            #V
            child.append("X")   #X = the mark of done appending 
            output.append( sum(c.val for c in child[:x]) / len(child[:x]) ) #calculate average value
            child = child[x+1:]  #clear node in previous level
            
        return output