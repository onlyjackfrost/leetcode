class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        #think this shity problem over 20min 
        #found out that if a != b, the uncommen subsequence is itself
        if a == b:
            return -1
        else:
            return max(len(a), len(b))