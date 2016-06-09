class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = {}
        result = 0;
        for i in nums:
            if i in ret:
                ret[i]=0;
            else:
                ret[i]=1;

        for v in ret.keys():
            if(ret[v]==1): 
                result = v

        return result