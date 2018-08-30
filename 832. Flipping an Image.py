class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        def flip(row):
            output_row = []
            for i in range(len(row)-1,-1,-1):
                if row[i] == 1:
                    num = 0
                if row[i] == 0:
                    num =1
                output_row.append(num)
            return output_row
        
        output=[]
        for row in A:
            output_row = flip(row)
            output.append(output_row)   
        return output