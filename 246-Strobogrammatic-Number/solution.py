class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        acceptable = ['1','6','9','8','0']
        counter = {}
        for c in acceptable:
            if c is '6':
                counter[c] = '9'
            elif c is '9':
                counter[c] = '6'
            else:
                counter[c] = c

        for i in range(len(num)):
            if num[i] in counter:
                if num[len(num)-i-1] != counter[num[i]]:
                    return False
            else:
                return False
        return True
        