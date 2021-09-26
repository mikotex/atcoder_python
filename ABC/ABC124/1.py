x,y = map(int,input().split())	

a1 = max(x, y)
if a1 == x:
    x -= 1
else :
    y -= 1

a2 = max(x,y)

print(a1+a2)