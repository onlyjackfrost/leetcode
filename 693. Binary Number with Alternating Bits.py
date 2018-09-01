class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        binary = bin(n)[2:]
        
        for i in range(len(binary)-1):
            if binary[i] == binary[i+1] : #check the bit on the right is the same or not
                return False
        return True