class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # pretty tricky to me, have to find out what kind of situation is the one that i'll definitely lose
        # if n = 4 i'll definitely lose, the same if n=8...
        #     =>  n%4 ==0 is the situation that i'll definitely lose
        if n%4==0 :
            return False
        else:
            return True