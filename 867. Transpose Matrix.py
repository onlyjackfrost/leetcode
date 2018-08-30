class Solution:
    def transpose(self, A):
        import numpy as np
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        len_col = len(A)
        len_raw = len(A[0])

        transpose = []
        for i in range(len_raw):
            transpose.append([])

        for i in range(len_raw):
            for j in range(len_col):
                transpose[i].append(A[j][i])
        return transpose