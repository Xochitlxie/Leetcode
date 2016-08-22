class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        acceptNumber = ["1","6","9","8","0"]
        counter = {}
        for i in acceptNumber:
            if i == "6":
                counter[i] = "9"
            elif i== "9":
                counter[i] = "6"
            else:
                counter[i] = i
        for i in range(len(nums)):
            if num[i] in acceptNumber:
                if counter[i] != len(num)-i-1:
                    return False
            else:
                return False
        return True