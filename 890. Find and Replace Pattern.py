class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def format(string):
            dic = {}
            output=''
            for cha in string:
                if string.count(cha)==1 :
                    output += "e"
                else :
                    if cha in dic:
                        output += dic[cha]
                    else:
                        dic[cha] = str(string.find(cha))
                        output += dic[cha]
            return output
        
        output = []
        pattern = format(pattern)
        for word in words:
            tmp = format(word)
            if tmp == pattern:
                output.append(word)
        return output