class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lists =['' for i in range(numRows)]
        for c,i in zip(s,self.getIndex(numRows)):
            
            lists[i]=  lists[i] + c
            
        return ''.join(lists)
            
        
    
    def getIndex(self, numRows):
        index =0
        operation = 1
        
        while True:
            yield index
            if numRows == 1:
                continue
            
            if (index == 0):
                operation = 1
            elif index == numRows -1:
                operation = -1
            index += operation
        
        
s = Solution()
print(s.convert("AB",1))