import math
n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

s = [a, b, c, d, e]
mins = min(s)
ans = math.floor((n-0.5)/mins) + len(s)

print(ans)