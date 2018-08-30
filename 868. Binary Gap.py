class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = bin(N)[2:]
        index = []
        distance_list = []
        for i , element in enumerate(binary):
            if element == "1" :
                index.append(i)
        for i in range(0,len(index)-1):
            distance = abs(index[i]-index[i+1] )
            distance_list.append(distance)
        if len(index) <=1:
            output = 0
        else:
            output = max(distance for distance in distance_list)
        return output
        