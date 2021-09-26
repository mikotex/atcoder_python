s=int(input())

li = list(map(int,input().split()))
li.sort()
cnt = 0
import bisect
for a in range(len(li)):
    for b in range(a + 1, len(li)):
       i = bisect.bisect_left(li, li[a]+li[b])
       cnt += i - b

print(cnt)