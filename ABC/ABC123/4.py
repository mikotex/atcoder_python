import sys
sys.setrecursionlimit(10000)
x,y,z,n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))

a.sort(reverse = True)
b.sort(reverse = True)
c.sort(reverse = True)

data = []
queue = [a[0]+b[0]+c[0]]

aqueue = [0]
bqueue = [0]
cqueue = [0]

global cnt
cnt = []

maxa=0
maxb=0
maxc=0

def queues(ai, bi, ci):
    global maxa, maxb, maxc
    if(maxa < ai+1):
        queue.append(a[ai + 1] + b[bi] + c[ci])
        aqueue.append(ai + 1)
        bqueue.append(bi)
        cqueue.append(ci)
        maxa = max(ai+1 , maxa)
    if(maxb < bi+1):
        queue.append(a[ai] + b[bi + 1] + c[ci])
        aqueue.append(ai)
        bqueue.append(bi + 1)
        cqueue.append(ci)
        maxb = max(bi + 1 , maxb)
    if(maxc < ci+1):
        queue.append(a[ai] + b[bi] + c[ci + 1])
        aqueue.append(ai)
        bqueue.append(bi)
        cqueue.append(ci + 1)
        maxc=max(ci+1,maxc)
    index = max(zip(queue, range(len(queue))))[1]
    print(queue.pop(index))
    cnt.append(1)
    if (len(cnt) == n):
        exit()
    ai2 = aqueue.pop(index)
    bi2 = bqueue.pop(index)
    ci2 = cqueue.pop(index)
    queues(ai2,bi2,ci2)


queues(0,0,0)
