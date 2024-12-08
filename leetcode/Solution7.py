class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        rle = ["1"]
        if n==1:
            return rle[0]
        
        for i in range(1,n):
            rle.append(self.count(rle[i-1]))
        
        return rle[n-1]
    def count(self,str1):
        count =0
        prev = ''
        output=''
        
        for s in str1:
            if s!=prev:
                if count>0:
                    output = output + str(count)+prev
                count=1
                prev=s
                continue
            count+=1
        output = output + str(count)+prev
        return output
    
s = Solution()
s.countAndSay(4)