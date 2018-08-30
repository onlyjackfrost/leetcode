class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        b_x = "{0:b}".format(x)
        b_y = "{0:b}".format(y)
        #append zero
        if len(b_x) - len(b_y) > 0 :
            append=""
            count = len(b_x)-len(b_y)
            for i in range(count):
                append += "0"
            b_y = append + b_y
        elif len(b_x) - len(b_y) < 0 :
            append=""
            count = len(b_y)-len(b_x)
            for i in range(count):
                append += "0"
            b_x = append + b_x
        
        #count the hammindistance
        #if len(b_x)==len(b_y):
        output = 0
        for i in range(len(b_x)):
            if b_x[i] != b_y[i] :
                output += 1
        
        return output