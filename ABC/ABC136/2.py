s=input()

a=int(s)

n = len(s)

m = int((n) /2)

ans = 0
for i in range(m):
    ans += 9 * (100 ** i)

if(n % 2 == 1):
    ans += a - 10 ** (n-1) + 1

print(ans)
