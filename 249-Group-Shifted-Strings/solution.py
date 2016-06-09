class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dictionary = {}
        for i in strings:
            hs = self.strHash(i)
            if hs not in dictionart.keys():
                dictionart[hs] = [str(i)]
            else:
                self.insertStr(dictionary[hs],str(i)
        return [dictionary[key] for key in dictionart.keys()]
        
        def strHash(self,astring):
            hslist = [(ord(i) - ord(asrting)[0]))%26 for i in astring]
            return tuple(hslist)