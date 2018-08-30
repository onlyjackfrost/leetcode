class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        dic = {}
        charlist = "abcdefghijklmnopqrstuvwxyz"
        for i in range(26) :
            dic[ charlist[i] ] = widths[i]
        
        rest = 100
        lines = 1
        for char in S :
            if rest - dic[char] < 0 :
                rest = 100
                lines += 1
                rest -= dic[char]
            else :
                rest -= dic[char]
        output = [lines, 100-rest]
        return output