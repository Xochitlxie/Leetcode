class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        arr = []
        for i in range(num+1):
            binary = bin(i)[2:]
            ones = binary.replace("0","")
            count = len(ones)
            arr.append(count)
        return arr