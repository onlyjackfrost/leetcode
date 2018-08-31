class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums)*len(nums[0]) == r * c : #if number of data in new matrix is right
            
            flatten =[nums[r][c] for r in range(len(nums)) for c in range(len(nums[0]))]  #flatten origin matrix
            output = [flatten[row*c : row*c+c] for row in range(r)]
            return output
        else :                              #else return original matrix
            return nums