import heapq 
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        minHeap = []
        maxHeap = []
        
        num1iter = iter(nums1)
        num2iter = iter(nums2)
        
        

class MaxHeap():
   
    def heahpush(self, li, item):
        heapq.heappush(li,-item)
    
    def heappop(self, li):
        -heapq.heappop(li)
    
    def heappushpop(li,item):
        a = heapq.heappushpop(li,-item)
        return -a
    
    def heapreplace(self, li, item):
        a = heapq.heapreplace(li,-item)
        return -a;
                