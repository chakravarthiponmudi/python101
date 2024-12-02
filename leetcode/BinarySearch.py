import time
def search(li, n,start,end) :
    if start<=end: 
        mp = start + int((end-start)/2)
        if li[mp] > n :
            return search(li,n,start,mp-1)
        elif li[mp] < n:
            return search(li,n,mp+1,end)
        elif li[mp] == n:
            return mp
    
    return

def searchwithLoop(li, n):
    start,end = 0,len(li)-1
    while start<=end :
        mp = start +int((end-start)/2)
        if li[mp] > n:
            end = mp-1
        elif li[mp] < n:
            start=mp+1
        elif li[mp] == n:
            return mp
    return 

start = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
c=[i for i in range(88888888)]
end = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
print('array intialisation time :', int((end-start)/1000000), 'ms')
s = 9
start = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
index = search(c,s,0,len(c)-1)
end = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
print(index, end-start, "ns")

start = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
index = searchwithLoop(c,s)
end = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
print(index, end-start, "ns")

    
    