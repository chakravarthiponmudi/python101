import time
from bisect import bisect_right
class Ratelimiter():
    def __init__(self, threshold, timeWindowInSecs):
        self.threshold = threshold
        self.timeWindow = timeWindowInSecs*1000
        self.queue = []
        
        
    def isAllowed(self):
        now = round(time.clock_gettime_ns(time.CLOCK_BOOTTIME) / 1000000,0)
        index = bisect_right(self.queue, now - self.timeWindow)
        self.queue = self.queue[index:]
        if len(self.queue) < self.threshold :
            self.queue.append(now)
            # print("ALLOWED")
            return True
        
        # print("BLOCKED")
        return False
    
    

r = Ratelimiter(100000,5)
i = 1
allowed = 0
blocked = 0
while i < 1000000:
    # time.sleep(1)
    if i%10000==0:
        print('procesed :', i, time.clock_gettime(time.CLOCK_REALTIME))
    if r.isAllowed():
        allowed+=1
    else:
        blocked+=1
    i+=1
        
print(allowed, blocked)
        
            
            
            
        
        