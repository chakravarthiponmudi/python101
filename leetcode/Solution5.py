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
        itemCount = 0
        heapqMax = MaxHeap()

        for item in self.read_smallest(nums1,nums2) :
            if itemCount %2 == 0 :
                if len(minHeap) == 0 :
                    heapqMax.heappush(maxHeap,item)
                else:
                    item1 = heapq.heapreplace(minHeap,item)
                    heapqMax.heappush(maxHeap,item1)
                itemCount += 1
                continue

            heapq.heappush(minHeap,item)
            
            itemCount += 1

        if itemCount %2 == 0:
            return (heapq.heappop(minHeap) + heapqMax.heappop(maxHeap))/2
        else:
            return heapqMax.heappop(maxHeap)


        
        
    def read_smallest(self, a1, a2):
        i,j=0,0
        while i<len(a1) and  j<len(a2) :
            if a1[i]<a2[j] :
                yield a1[i]
                i+=1
            else:
                yield a2[j]
                j+=1

        while i<len(a1) :
            yield a1[i]
            i+=1
        
        while j<len(a2) :
            yield a2[j]
            j+=1


        
        

class MaxHeap():
   
    def heappush(self, li, item):
        heapq.heappush(li,-item)
    
    def heappop(self, li):
        return -heapq.heappop(li)
    
    def heappushpop(li,item):
        a = heapq.heappushpop(li,-item)
        return -a
    
    def heapreplace(self, li, item):
        a = heapq.heapreplace(li,-item)
        return -a;
                

s = Solution()
a = [1,2]
b = [3,4]

print(s.findMedianSortedArrays(a,b))