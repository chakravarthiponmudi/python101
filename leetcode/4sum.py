class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        formedSet = set()
        ans = []
        l = len(nums)
        for i in range(l-3):
            for j in range(i+1,l-2):
                lo,hi =j+1,l-1
                while lo<hi :
                    sum = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if sum == target:
                        if not self.foundInSet(formedSet,[nums[i],nums[j],nums[lo],nums[hi]]):
                            ans.append([nums[i],nums[j],nums[lo],nums[hi]])
                        lo = lo+1
                        hi=hi-1
                        continue
                    if sum<target:
                        lo = lo+1
                    else:
                        hi = hi -1
        return ans
    
    def foundInSet(self, s, l):
        k = ':'.join(map(str,l))
        if k in s:
            return True
        else:
            s.add(k)
            return False
    
s = Solution()

print(s.fourSum([1,0,-1,0,-2,2],0))
print(s.fourSum([2,2,2,2,2],8))

        