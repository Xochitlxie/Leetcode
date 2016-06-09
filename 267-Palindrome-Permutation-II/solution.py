class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dictKey = {}
        for a in s:
            dictKey[a] = dictKey.get(a,0) + 1
        double = []
        single = []
        if not self.checkPalindromes(s,dictKey,double,single):
            return []
        result = []
        n = len(s)/2
        self.generation(double,single,'',result,n)
        return list(set(result))
        
    def generation(self,double,single,string,result,n):
        if len(string) == n:
            if len(single) != 0:
                result.append(string+single[0]+string[::-1])
            else:
                result.append(string+string[::-1])
        for i in range(len(double)):
            self.generation(double[:i]+double[i+1:],single,string+double[i],result,n)
        
    def checkPalindromes(self,s,dictKey,double,single):
        if len(s)%2 == 0:
            for key in dictKey.keys():
                if dictKey[key]%2 == 1:
                    return False
                for i in range(dictKey[key]/2):
                    double.append(key)
        else:
            count = 0
            for key in dictKey.keys():
                if dictKey[key]%2 == 1:
                    count += 1
                    if count > 1:
                        return False
                    single.append(key)
                    for i in range(dictKey[key]/2):
                        double.append(key)
                else:
                    for i in range(dictKey[key]/2):
                        double.append(key)
        return True