class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        #https://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
        def isprime(n):  
            if n == 1:
                return False
            if n == 2:
                return True
            if n == 3:
                return True
            if n % 2 == 0:
                return False
            if n % 3 == 0:
                return False
            i = 5
            w = 2
            
            while i * i <= n:
                if n % i == 0:
                    return False
                i += w
                w = 6 - w
            return True
        
        output = 0
        for num in range(L,R+1):
            setbit = bin(num).count('1')  #count the set bits
            if isprime(setbit) == True :    #check set bits is prime or not
                output += 1  #if prime, count +1
        return output