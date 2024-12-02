class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for row_num in range(numRows):
            row = [None for _ in range(row_num+1)]  
            row[0],row[-1] = 1,1
            
            for j in range(1,len(row)-1):
                row[j] = triangle[1][j-1]+triangle[1][j]

            if row_num>1:
                del triangle[0]
                
            triangle.append(row)
            
        return triangle
            
            
s = Solution()
s.generate(1000)


            
            
                
                
        