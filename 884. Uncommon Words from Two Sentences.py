class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        dic = {}
        
        for word in A.split(" ") + B.split(" ") :
            if word in dic:
                dic[word] = dic[word] +1
            else :
                dic[word] = 1
        output = []
        for key, value in dic.items():
            if value == 1:
                output.append(key)
        return output
        