class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        location = []
        output = []
        for index in range(len(S)):
            if S[index] == C:
                location.append(index)
        for index in range(len(S)):
            distance = min(abs(l-index) for l in location )
            output.append(distance)
        return output