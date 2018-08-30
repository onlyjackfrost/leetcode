class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: 
            
            return None
        root = nums.index(max(nums))
        current_node = TreeNode(nums[root])
        
        current_node.left = self.constructMaximumBinaryTree(nums[:root])
        current_node.right = self.constructMaximumBinaryTree(nums[root+1 :])
        
        return current_node
        