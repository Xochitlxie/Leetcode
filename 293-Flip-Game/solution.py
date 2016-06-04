class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        answer = []
        if len(s) < 2:
            return answer
        for i in range(0,len(s)-1):
            newString = ''
            if s[i]=='+' and s[i+1] == '+':
                newString = s[0:i] + '--' + s[i+2:len(s)]
                answer.append(newString)
        return answer