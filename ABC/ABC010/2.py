hash = [0, 1, 0, 1, 2, 3]

a=int(input())
li = list(map(int,input().split()))
ans = 0
for i in range(len(li)):
    ans += hash[(li[i] % 6) - 1]

print(ans)