class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        acceptNumber = ["1","6","9","8","0"]
        counter = {}
        for i in acceptNumber:
            if c=="6":
                counter[c] == "9"
            elif c== "9":
                counter[c] == "6"
            else:
                counter[c] == c
        for i in range(len(nums)):
            if nums[i] in acceptNumber:
                if counter[i] != len(nums)-i-1:
                    return False
            else:
                return False
        return True