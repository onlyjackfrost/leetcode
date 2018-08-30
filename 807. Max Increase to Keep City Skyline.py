class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sky_top = []
        sky_left = []
        
        for j in range(len(grid)):
            sky_left.append(max(grid[j]))
        for i in range(len(grid[0])):    
            col = []
            for j in range(len(grid)):
                col.append(grid[j][i])
            sky_top.append(max(col))
        
        output = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])): 
                sky_value = min(sky_top[i], sky_left[j])
                output += (sky_value - grid[i][j])
        return output