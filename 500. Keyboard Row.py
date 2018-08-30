class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row = [["q","w","e","r","t","y","u","i","o","p"], ["a","s","d","f","g","h","j","k","l"], ["z","x","c","v","b",'n','m']]
        output = words
        for j in range(len(words)-1,-1,-1):
            word = words[j]
            first = 1
            statue = -1
            tmp = -1
            remove = 0
            lower = word.lower()
            for cha in lower:
                if first ==1 :
                    first = 0
                    for i in range(len(row)):
                        if cha in row[i]:
                            statue = i
                    continue
                        
                else:
                    if cha in row[statue]:
                        continue
                    if cha not in row[statue]:
                        remove = 1
            if remove == 1:
                output.remove(word)     
        return output