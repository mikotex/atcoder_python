x,y = map(int,input().split())
li = list(map(int,input().split()))

for day in li:
    x -= day

if x < 0:
    print(-1)
else:
    print(x)