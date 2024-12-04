class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        number_yet_get = True
        isNegative = False
        
        ans=0
        for i in self.getNextNumber(s):
            if i == -1:
                isNegative = True
                continue
        
            if i ==0 and number_yet_get:
                continue
            if not number_yet_get:
                ans = ans * 10
                
            number_yet_get = False
            ans = ans + i
            if isNegative and (ans * -1) <= -2147483648:
                return -2147483648
            elif not isNegative and  ans >= 2147483647:
                return  2147483647
            
            
        if isNegative:
            return ans * -1
        return ans
            
    
    def getNextNumber(self, s):
        no_char_found = True
        for c in s:
            num = ord(c) - ord('0')          
            if num >=0 and num <=9 :
                no_char_found = False
                yield num
            elif c == ' ' and no_char_found:
                continue
            elif c == '+' and no_char_found:
                no_char_found = False
                continue
            elif c =='-' and no_char_found:
                no_char_found = False
                yield -1
            else:
                return
            
s = Solution()
print(s.myAtoi("-2147483647"))