# https://leetcode.com/problems/divide-array-into-equal-pairs/

from collections import Counter

class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) % 2 != 0:
            return False
        
        counter = Counter()
        for e in nums:
            counter[e] += 1
        
        inValidElements = [i for i in counter if counter[i]%2 != 0]
        return len(inValidElements) == 0
    
s = Solution()
print(s.divideArray([3,2,3,2,2,2]))