class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #檢查每個data是1的點的上下左右有幾個1，計算該點的perimeter
        perimeter = 0
        for j in range(len(grid)):
            for i in range(len(grid[0])):
                if grid[j][i] == 1:
                    cnt=0  #init
                    if j<len(grid)-1: #index error
                        if grid[j+1][i] == 1:
                            cnt+=1
                    if i<len(grid[0])-1:  #index error
                        if grid[j][i+1] == 1:
                            cnt+=1
                    if j>=1:
                        if grid[j-1][i] == 1:
                            cnt+=1
                    if i>=1:
                        if grid[j][i-1] == 1:
                            cnt+=1
                    #取得該點的perimeter
                    if cnt == 1:
                        perimeter += 3
                    if cnt == 2:
                        perimeter += 2
                    if cnt == 3:
                        perimeter += 1
                    if cnt == 0:
                        perimeter += 4
      
        return perimeter