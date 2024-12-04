class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start,end = 0, len(height)-1
        vol = 0
        while start < end:
            h = min(height[start],height[end])
            vol =max(vol, (end-start)*h)
            if (height[start] <= height[end]):
                start += 1
            else:
                end -=1
        return vol
                
s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))