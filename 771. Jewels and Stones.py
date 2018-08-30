class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        num = 0
        for charactor in J :
            tmp = S.count(charactor)
            num += tmp
        return num