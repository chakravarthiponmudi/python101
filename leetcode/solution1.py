class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
        n = len(arr)

        # create a 2D array of n x n
        diff = [[0] * n for i in range(n)]
        for i in range(n - 1):
            for j in range(i+1, n):
                diff[i][j] = abs(arr[i] - arr[j])

        count = 0
        for i in range(n - 2):
            for j in range(i+1, n - 1):
                if diff[i][j] <= a:
                    for k in range(j+1, n):
                        if (diff[j][k] <= b
                        and diff[i][k] <= c):
                            # Good triplet!!
                            count += 1
        return count
    
s = Solution()
print(s.countGoodTriplets([3,0,1,1,9,7],7,2,3))
a = [1,'a',2.3]
b=a[0]
b+=1
print(b)
b=a[1]
print(b)
print(a)