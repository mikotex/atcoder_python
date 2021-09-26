li = input().split()
n = int(li[0])
t = int(li[1])

maxt = 1001
cost = 1001
ans = 1001

for i in range(0, n):
    li = input().split()
    x = int(li[0])
    y = int(li[1])
    if y <= t:
        if x <= cost:
            cost = x

if cost == 1001:
    print("TLE")
else:
    print(cost)