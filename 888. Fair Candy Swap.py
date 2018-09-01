class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # pass 64/75 of test data, hit the time limit
        
        final = (sum(A) + sum(B))/2
        
        for candy in set(A):
            target = final - sum(A) + candy
            if target in set(B):
                return[candy, target]
        