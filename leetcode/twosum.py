class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i,n in enumerate(nums):
            complement = target - n
            if n in dict:
                return [dict[n],i]
            else:
                dict[complement] = i
                
s = Solution()
print(s.twoSum([2,7,11,15],9))