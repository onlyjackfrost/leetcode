class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        output = []
        dic={}
        for cpdomain in cpdomains :
            num = cpdomain.split(' ')[0]
            level_domain = cpdomain.split(' ')[1].split('.')
            domain = ""
            for i in range(len(level_domain)-1, -1, -1):
                domain = level_domain[i]+domain
                if domain not in dic:    
                    dic[domain] = num
                else :
                    dic[domain] = str(int(dic[domain]) + int(num))
                domain = "." + domain
        for key, value in dic.items():
            output.append(value+" "+key)
        return output