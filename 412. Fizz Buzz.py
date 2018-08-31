class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output=[]

        for i in range(1,n+1):

            tmp = ""    #init output string
            if i % 3 == 0:   
                tmp += "Fizz"    
            
            if i % 5 == 0:
                tmp += "Buzz"
            
            if tmp == "" : #i is not divisible by 3 and 5
                tmp += str(i)
            output.append(tmp)
        return output